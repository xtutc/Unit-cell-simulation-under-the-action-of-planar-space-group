from ase import Atoms

def generate_res_file(output_path, atoms):
    """
    生成 Material Studio 可识别的 .res 文件

    参数:
    - output_path: 输出文件路径（例如：'structure.res'）
    - atoms: ASE 的 Atoms 对象
    """

    # 生成标题行
    titl_line = f"TITL -1"

    # 获取晶胞参数
    cell_params = atoms.get_cell_lengths_and_angles()
    cell_line = (
        f"CELL  0.0000  "  
        f"{cell_params[0]:.4f}  {cell_params[1]:.4f}  {cell_params[2]:.4f} "
        f"{cell_params[3]:.4f}  {cell_params[4]:.4f}  {cell_params[5]:.4f}"
    )

    # 生成 LATT 行
    latt_line = "LATT -1"

    # 获取唯一元素列表（这里要求顺序与 MS 中的要求一致）
    elements = sorted(set(atoms.get_chemical_symbols()))
    sfac_line = "SFAC " + " ".join(elements)

    # 生成原子行
    atom_lines = []
    # 构建 SFAC 映射，例如：{'B': 1, 'C': 2, 'N': 3, 'O': 4}
    sfac_mapping = {element: i + 1 for i, element in enumerate(elements)}
    scaled_positions = atoms.get_scaled_positions()
    symbols = atoms.get_chemical_symbols()

    # 对每个原子生成类似 "O1    4    0.83159    0.84948    0.21191    1.00000   0.00000" 的行
    for idx, (symbol, (x, y, z)) in enumerate(zip(symbols, scaled_positions), 1):
        sfac_index = sfac_mapping[symbol]
        atom_line = (
            f"{symbol}{idx:<4d} {sfac_index:<4d} "  # 原子编号及 SFAC索引，注意这里我们格式化输出使其占用固定宽度
            f"{x:10.5f} {y:10.5f} {z:10.5f} "      # 分数坐标
            f"1.00000 0.00000"                     # 占据率和温度因子
        )
        atom_lines.append(atom_line)

    # 组合所有文件内容
    content = [
        titl_line,
        cell_line,
        latt_line,
        sfac_line,
        *atom_lines,
        "END"
    ]

    # 写入文件（使用 Windows 换行符）
    with open(output_path, 'w', newline='\r\n') as f:
        f.write("\n".join(content))


