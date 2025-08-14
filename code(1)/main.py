# -*- coding: utf-8 -*-
import sys
# 添加 ase 所在的 site-packages 目录（从 pip 输出中获取）
sys.path.append("/public/physics2023/202305710506/py3.8.5/lib/python3.6/site-packages")

import numpy as np
from math import sin, cos, pi, sqrt
from ase import Atoms
from res_generate import generate_res_file
from point_group import point_group_opearation

# ==================== 配置参数 ====================
rand = np.random.default_rng()
CELL_SIZE = 30  # 晶胞尺寸（Å）
MAX_TRIES = 100  # 生成有效原子的最大尝试次数
DISTANCE_FACTOR = 0.8  # 距离因子，控制最小距离与半径的比例关系


# ==================== 核心函数 ====================
def generate_atoms(r):
    """生成单个围绕原点的随机原子坐标（球坐标系）"""
    theta = np.random.uniform(0, pi)  # 极角（0~π）
    phi = np.random.uniform(0, 2 * pi)  # 方位角（0~2π）
    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)
    return np.array([x, y, z])  # 直接返回NumPy数组


def calculate_min_distance(r, target_atoms):
    """根据当前半径计算动态最小距离"""
    # 使用半径的函数计算最小距离，保持与原子数的关系
    return DISTANCE_FACTOR * sqrt(4 / target_atoms * r ** 2)


def generate_valid_base(existing, r, target_atoms):
    """生成与已有原子距离≥MIN_DISTANCE的新基础原子"""
    min_distance = calculate_min_distance(r, target_atoms)

    for _ in range(MAX_TRIES):
        new_pos = generate_atoms(r)  # 生成NumPy数组
        # 检查与所有已有原子的距离（已有原子均为NumPy数组）
        if all(np.linalg.norm(new_pos - pos) >= min_distance for pos in existing):
            return new_pos
    raise RuntimeError("无法在{}次内生成有效基础原子".format(MAX_TRIES))


def apply_group_operations(base_pos, point_group):
    """应用点群所有操作生成对称原子（返回NumPy数组）"""
    operations = point_group_opearation.get(point_group, [])
    if not operations:
        raise ValueError("点群{}无操作定义".format(point_group))

    # 应用所有操作生成对称原子（保持NumPy数组类型）
    transformed = np.array([np.dot(base_pos, op['rotation']) for op in operations])

    # 去重：四舍五入到6位小数后去重（返回NumPy数组）
    transformed_rounded = np.around(transformed, decimals=6)
    _, unique_indices = np.unique(transformed_rounded, axis=0, return_index=True)
    unique_transformed = transformed[np.sort(unique_indices)]

    return unique_transformed  # 返回NumPy数组（形状：(操作数, 3)）


# ==================== 主程序 ====================
if __name__ == "__main__":
    center = np.array([CELL_SIZE / 2] * 3)  # 晶胞中心坐标（NumPy数组）
    struct_idx = 0  # 添加struct_idx初始化（原代码缺少）

    for struct_idx in range(0,1000000):  # 移除括号，Python 3.6兼容
        RADIUS_MIN, RADIUS_MAX = 3.5, 4.0  # 原子生成半径范围（Å）
        TARGET_ATOMS = rand.integers(50, 71)  # 目标原子数（随机50-70）

        pos_list = []  # 移除类型注解，Python 3.6不支持list[np.ndarray]语法
        # 随机选择一个有操作的点群（假设点群1-32均有定义）
        point_group_list = [g for g in point_group_opearation if g in range(1, 33)]
        point_group = np.random.choice(point_group_list)
        # 替换f-string为format格式
        print("\n=== 生成结构{}，使用点群{}，目标{}原子 ===".format(
            struct_idx + 1, point_group, TARGET_ATOMS
        ))

        while len(pos_list) < TARGET_ATOMS:
            try:
                # 生成有效基础原子（NumPy数组）
                r = rand.uniform(RADIUS_MIN, RADIUS_MAX)  # 直接使用浮点数
                base_pos = generate_valid_base(pos_list, r, TARGET_ATOMS)
                current_min_distance = calculate_min_distance(r, TARGET_ATOMS)
            except RuntimeError as e:
                print("警告：{}，当前原子数{}，提前终止".format(e, len(pos_list)))
                break

            # 应用点群操作并去重（返回NumPy数组）
            new_group = apply_group_operations(base_pos, point_group)
            # 过滤与现有原子距离过近的新原子（使用当前半径对应的最小距离）
            valid_new = [
                pos for pos in new_group  # pos是NumPy数组
                if all(np.linalg.norm(pos - existing) >= current_min_distance for existing in pos_list)
            ]
            if not valid_new:
                print("提示：当前基础原子生成的对称原子均重复，跳过")
                continue

            # 检查终止条件
            current = len(pos_list)
            new_count = len(valid_new)
            if current + new_count > TARGET_ATOMS:
                needed = TARGET_ATOMS - current
                pos_list.extend(valid_new[:needed])  # 扩展NumPy数组列表
                print("终止条件触发：添加{}原子（{}→{}）".format(
                    needed, current, current + needed
                ))
                break
            else:
                pos_list.extend(valid_new)  # 扩展NumPy数组列表
                print("添加{}原子，当前总数{}".format(new_count, current + new_count))

        # 调整坐标到晶胞中心并保存（所有坐标均为NumPy数组）
        pos_array = np.array(pos_list) + center  # 数组运算自动对齐
        atoms = Atoms(
            symbols=['C'] * len(pos_array),
            positions=pos_array,
            cell=[CELL_SIZE] * 3,
            pbc=True
        )
        res_path = "input/structure_{}.res".format(struct_idx + 1)
        generate_res_file(res_path, atoms)
        print("结构{}保存完成，实际原子数{}".format(
            struct_idx + 1, len(pos_array)
        ))

        struct_idx += 1  # 增加索引（避免无限循环时文件名重复）
