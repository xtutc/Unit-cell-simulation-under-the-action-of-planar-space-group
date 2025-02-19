def generate_res_file(output_path, title, cell_params, latt, elements, atoms_data):
    """
    生成Material Studio可识别的.res文件

    参数:
    - output_path: 输出文件路径（如：'structure.res'）
    - title: 结构标题（字符串）
    - cell_params: 晶胞参数元组 (a, b, c, alpha, beta, gamma, volume)
    - latt: LATT参数（字符串，如 '-1'）
    - elements: 元素列表（按SFAC顺序，如 ['B', 'C', 'N', 'O']）
    - atoms_data: 原子数据列表，每个元素为元组 (元素符号, x, y, z)
    """

    # 生成标题行
    titl_line = f"TITL {title}"

    # 生成CELL行（保留4位小数）
    cell_line = (
        f"CELL  {cell_params[0]:.4f}  {cell_params[1]:.4f}  {cell_params[2]:.4f} "
        f"{cell_params[3]:.4f}  {cell_params[4]:.4f}  {cell_params[5]:.4f} "
        f"{cell_params[6]:.4f}"
    )

    # 生成LATT行
    latt_line = f"LATT {latt}"

    # 生成SFAC行（元素后加0）
    sfac_line = "SFAC " + " ".join(elements) + " 0"

    # 生成原子行
    atom_lines = []
    sfac_mapping = {element: i + 1 for i, element in enumerate(elements)}

    for idx, (element, x, y, z) in enumerate(atoms_data, 1):
        sfac_index = sfac_mapping[element]
        atom_line = (
            f"{element}{idx} {sfac_index} "
            f"{x:.5f} {y:.5f} {z:.5f} "
            "1.00000 0.00000"  # 占据率和温度因子
        )
        atom_lines.append(atom_line)

    # 组合所有内容
    content = [
        titl_line,
        cell_line,
        latt_line,
        sfac_line,
        *atom_lines,
        "END\n"  # 必须包含END行
    ]

    # 写入文件（使用Windows换行符）
    with open(output_path, 'w', newline='\r\n') as f:
        f.write("\n".join(content))

    # 生成.res文件
    generate_res_file(
        output_path="output.res",
        title="Generated Structure",
        cell_params=cell_parameters,
        latt="-1",
        elements=elements_list,
        atoms_data=atoms
    )