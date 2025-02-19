import numpy as np
from pymatgen.io.cif import CifParser
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


def extract_float_or_default(value, default):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def cif_to_res(cif_file, res_file):
    try:
        # 解析 CIF 文件
        parser = CifParser(cif_file)
        structures = parser.get_structures()
        if not structures:
            print("No valid structure found in the CIF file.")
            return
        structure = structures[0]

        # 提取晶格参数
        lattice = structure.lattice
        a, b, c = lattice.a, lattice.b, lattice.c
        alpha, beta, gamma = lattice.alpha, lattice.beta, lattice.gamma

        # 获取 CIF 数据块
        cif_data = parser.as_dict()
        data_block = list(cif_data.values())[0]

        # 尝试获取 Z 值
        z_value = data_block.get("_cell_formula_units_Z", 1)
        try:
            z_value = int(z_value)
        except ValueError:
            print("Could not determine valid Z value. Using default (Z = 1).")
            z_value = 1

        # 处理对称性信息
        try:
            sga = SpacegroupAnalyzer(structure)
            spacegroup = sga.get_space_group_symbol()
            hall_symbol = sga.get_hall()
        except Exception as e:
            print(f"Error analyzing symmetry: {e}. Skipping symmetry information.")
            spacegroup = None
            hall_symbol = None

        # 提取原子信息
        atom_labels = data_block.get("_atom_site_label", [])
        atom_types = data_block.get("_atom_site_type_symbol", [])
        atom_frac_x = data_block.get("_atom_site_fract_x", [])
        atom_frac_y = data_block.get("_atom_site_fract_y", [])
        atom_frac_z = data_block.get("_atom_site_fract_z", [])
        atom_occupancies = data_block.get("_atom_site_occupancy", [])
        atom_U_iso_or_equiv = data_block.get("_atom_site_U_iso_or_equiv", [])

        # 检查各向异性位移参数
        anisotropic = "_atom_site_aniso_U_11" in data_block
        if anisotropic:
            U_11 = data_block["_atom_site_aniso_U_11"]
            U_22 = data_block["_atom_site_aniso_U_22"]
            U_33 = data_block["_atom_site_aniso_U_33"]
            U_12 = data_block["_atom_site_aniso_U_12"]
            U_13 = data_block["_atom_site_aniso_U_13"]
            U_23 = data_block["_atom_site_aniso_U_23"]

        # 处理无序结构
        disorder_groups = {}
        for i, label in enumerate(atom_labels):
            disorder_flag = data_block.get(f"_atom_site_disorder_group_{label}", None)
            if disorder_flag:
                if disorder_flag not in disorder_groups:
                    disorder_groups[disorder_flag] = []
                disorder_groups[disorder_flag].append(i)

        # 处理原子替代信息
        atom_substitutions = {}
        for key, value in data_block.items():
            if key.startswith("_atom_site_substitution_"):
                site_label = key.split("_")[-1]
                if site_label not in atom_substitutions:
                    atom_substitutions[site_label] = []
                atom_substitutions[site_label].append(value)

        # 处理键长和键角约束
        bond_lengths = []
        bond_angles = []
        if "_geom_bond_atom_site_label_1" in data_block:
            atom1_labels = data_block["_geom_bond_atom_site_label_1"]
            atom2_labels = data_block["_geom_bond_atom_site_label_2"]
            lengths = data_block["_geom_bond_distance"]
            for atom1, atom2, length in zip(atom1_labels, atom2_labels, lengths):
                bond_lengths.append((atom1, atom2, extract_float_or_default(length, 0.0)))

        if "_geom_angle_atom_site_label_1" in data_block:
            atom1_labels = data_block["_geom_angle_atom_site_label_1"]
            atom2_labels = data_block["_geom_angle_atom_site_label_2"]
            atom3_labels = data_block["_geom_angle_atom_site_label_3"]
            angles = data_block["_geom_angle"]
            for atom1, atom2, atom3, angle in zip(atom1_labels, atom2_labels, atom3_labels, angles):
                bond_angles.append((atom1, atom2, atom3, extract_float_or_default(angle, 0.0)))

        # 打开 RES 文件以写入
        with open(res_file, 'w') as f:
            # 写入标题行
            f.write("TITL Converted from CIF file\n")

            # 写入晶格参数
            f.write(f"CELL 1.0 {a:.6f} {b:.6f} {c:.6f} {alpha:.6f} {beta:.6f} {gamma:.6f}\n")

            # 写入 Z 值
            f.write(f"ZERR {z_value} 0 0 0 0 0 0\n")

            # 写入对称性信息
            if spacegroup and hall_symbol:
                f.write(f"SYMM {spacegroup}\n")
                f.write(f"SFAC {','.join(set(atom_types))}\n")
                f.write(f"HKLF 4\n")
                f.write(f"Hall {hall_symbol}\n")

            # 写入原子信息
            for i in range(len(atom_labels)):
                element = atom_types[i]
                x = extract_float_or_default(atom_frac_x[i], 0.0)
                y = extract_float_or_default(atom_frac_y[i], 0.0)
                z = extract_float_or_default(atom_frac_z[i], 0.0)
                occupancy = extract_float_or_default(atom_occupancies[i] if i < len(atom_occupancies) else 1.0, 1.0)
                U_iso = extract_float_or_default(atom_U_iso_or_equiv[i] if i < len(atom_U_iso_or_equiv) else 0.01, 0.01)

                disorder_group = None
                for group, indices in disorder_groups.items():
                    if i in indices:
                        disorder_group = group
                        break

                if anisotropic:
                    U11 = extract_float_or_default(U_11[i], 0.01)
                    U22 = extract_float_or_default(U_22[i], 0.01)
                    U33 = extract_float_or_default(U_33[i], 0.01)
                    U12 = extract_float_or_default(U_12[i], 0.0)
                    U13 = extract_float_or_default(U_13[i], 0.0)
                    U23 = extract_float_or_default(U_23[i], 0.0)
                    if disorder_group:
                        f.write(
                            f"ANIS {element:2s} {x:.6f} {y:.6f} {z:.6f} {occupancy:.4f} {U11:.6f} {U22:.6f} {U33:.6f} {U12:.6f} {U13:.6f} {U23:.6f}  D{disorder_group}\n")
                    else:
                        f.write(
                            f"ANIS {element:2s} {x:.6f} {y:.6f} {z:.6f} {occupancy:.4f} {U11:.6f} {U22:.6f} {U33:.6f} {U12:.6f} {U13:.6f} {U23:.6f}\n")
                else:
                    if disorder_group:
                        f.write(
                            f"ATOM {element:2s} {x:.6f} {y:.6f} {z:.6f} {occupancy:.4f} {U_iso:.6f}  D{disorder_group}\n")
                    else:
                        f.write(f"ATOM {element:2s} {x:.6f} {y:.6f} {z:.6f} {occupancy:.4f} {U_iso:.6f}\n")

            # 写入原子替代信息
            for site_label, substitutions in atom_substitutions.items():
                for sub in substitutions:
                    f.write(f"SUB {site_label} {sub}\n")

            # 写入键长和键角约束
            for atom1, atom2, length in bond_lengths:
                f.write(f"DIST {atom1} {atom2} {length:.6f}\n")
            for atom1, atom2, atom3, angle in bond_angles:
                f.write(f"ANGL {atom1} {atom2} {atom3} {angle:.6f}\n")

        print(f"Conversion completed. RES file saved as {res_file}")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")


