import numpy as np
import pandas as pd
from ase import Atoms
from ase.io import write
from oblique_crystal import oblique_cell
from rectangular_crystal import rectangular_cell
from tetragonal_crystal import tetragonal_cell
from hexagonal_crystal import hexagonal_cell
from p1 import p1_generate_atoms_structure
from p2 import p2_generate_atoms_structure
from p1m1 import p1m1_generate_atoms_structure
from p1g1 import p1g1_generate_atoms_structure
from c1m1 import c1m1_generate_atoms_structure
from p2mm import p2mm_generate_atoms_structure
from p2mg import p2mg_generate_atoms_structure
from p2gg import p2gg_generate_atoms_structure
from c2mm import c2mm_generate_atoms_structure
from p4 import p4_generate_atoms_structure
from p4mm import p4mm_generate_atoms_structure
from p4gm import p4gm_generate_atoms_structure
from p3 import p3_generate_atoms_structure
from p3m1 import p3m1_generate_atoms_structure
from p31m import p31m_generate_atoms_structure
from p6 import p6_generate_atoms_structure
from p6mm import p6mm_generate_atoms_structure


# 计算并输出距离矩阵到 Excel 文件
def compute_distance_matrix(atoms, output_file):
    distances = atoms.get_all_distances(mic=True)  # mic=True会考虑周期性边界条件
    num_atoms = len(atoms)
    atom_labels = [f"Atom_{i}" for i in range(num_atoms)]
    distance_df = pd.DataFrame(distances, index=atom_labels, columns=atom_labels)
    distance_df.to_excel(output_file, sheet_name='Distance Matrix')
    print(f"距离矩阵已保存到 {output_file}")

# 保存CIF文件并计算距离矩阵
def save_structure_and_compute_distances(atom, cif_path, distance_matrix_path):
    if atom is not None:
        write(cif_path, atom)
        print(f"已将原子结构保存到 {cif_path}")
        compute_distance_matrix(atom, distance_matrix_path)
    else:
        print("Error: 未生成原子结构。")

# 主函数：生成随机晶体结构
def main():
    rand = np.random.default_rng()
    space_group_number = rand.integers(1, 18)
    print(f"随机选择的空间群: 第{space_group_number}个空间群")

    num_atoms = rand.integers(10, 100)
    print(f"生成的原子数量: {num_atoms}")
    scale_position = rand.random((num_atoms, 3))

    # 定义路径
    cif_path = r"C:\Users\Xtulyd\OneDrive\Desktop\study exercise\second exercise\structual\Untitled_Files\Documents\output.cif"
    distance_matrix_path = r"C:\Users\Xtulyd\OneDrive\Desktop\study exercise\second exercise\项目\distance_matrix.xlsx"

    # 空间群对应的原子生成函数
    space_group_functions = {
        1: p1_generate_atoms_structure,
        2: p2_generate_atoms_structure,
        3: p1m1_generate_atoms_structure,
        4: p1g1_generate_atoms_structure,
        5: c1m1_generate_atoms_structure,
        6: p2mm_generate_atoms_structure,
        7: p2mg_generate_atoms_structure,
        8: p2gg_generate_atoms_structure,
        9: c2mm_generate_atoms_structure,
        10: p4_generate_atoms_structure,
        11: p4mm_generate_atoms_structure,
        12: p4gm_generate_atoms_structure,
        13: p3_generate_atoms_structure,
        14: p3m1_generate_atoms_structure,
        15: p31m_generate_atoms_structure,
        16: p6_generate_atoms_structure,
        17: p6mm_generate_atoms_structure
    }

    # 获取对应的原子生成函数
    if space_group_number in space_group_functions:
        # 根据空间群选择晶体类型
        if space_group_number in [1, 2]:
            atom = space_group_functions[space_group_number](oblique_cell, scale_position, 0.1, 'random')
        elif space_group_number in [3, 4, 5, 6, 7, 8, 9]:
            atom = space_group_functions[space_group_number](rectangular_cell, scale_position, 0.1, 'random')
        elif space_group_number in [10, 11, 12]:
            atom = space_group_functions[space_group_number](tetragonal_cell, scale_position, 0.1, 'random')
        else:
            atom = space_group_functions[space_group_number](hexagonal_cell, scale_position, 0.1, 'random')

        # 保存结构并计算距离矩阵
        save_structure_and_compute_distances(atom, cif_path, distance_matrix_path)


    else:
        print(f"空间群 {space_group_number} 暂未实现。")

if __name__ == "__main__":
    main()