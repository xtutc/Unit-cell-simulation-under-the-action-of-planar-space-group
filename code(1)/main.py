import numpy as np
from math import sin, cos, pi
from ase import Atoms
from res_generate import generate_res_file
from point_group import point_group_opearation

# ==================== 配置参数 ====================
rand = np.random.default_rng()
CELL_SIZE = 30  # 晶胞尺寸（Å）
MIN_DISTANCE = 0.4  # 原子最小间距（Å）
MAX_TRIES = 100  # 生成有效原子的最大尝试次数


# ==================== 核心函数 ====================
def generate_atoms(r: float) -> np.ndarray:
    """生成单个围绕原点的随机原子坐标（球坐标系）"""
    theta = np.random.uniform(0, pi)  # 极角（0~π）
    phi = np.random.uniform(0, 2 * pi)  # 方位角（0~2π）
    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)
    return np.array([x, y, z])  # 直接返回NumPy数组


def generate_valid_base(existing: list[np.ndarray], r: float) -> np.ndarray:
    """生成与已有原子距离≥MIN_DISTANCE的新基础原子"""
    for _ in range(MAX_TRIES):
        new_pos = generate_atoms(r)  # 生成NumPy数组
        # 检查与所有已有原子的距离（已有原子均为NumPy数组）
        if all(np.linalg.norm(new_pos - pos) >= MIN_DISTANCE for pos in existing):
            return new_pos
    raise RuntimeError(f"无法在{MAX_TRIES}次内生成有效基础原子")


def apply_group_operations(base_pos: np.ndarray, point_group: int) -> np.ndarray:
    """应用点群所有操作生成对称原子（返回NumPy数组）"""
    operations = point_group_opearation.get(point_group, [])
    if not operations:
        raise ValueError(f"点群{point_group}无操作定义")

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

    for struct_idx in range(1000000000):
        RADIUS_RANGE = (3.5, 4.0)  # 原子生成半径范围（Å）
        TARGET_ATOMS = rand.integers(20, 80)  # 目标原子数（随机20-80）
        pos_list: list[np.ndarray] = []  # 明确存储NumPy数组的列表
        # 随机选择一个有操作的点群（假设点群1-32均有定义）
        point_group = np.random.choice([g for g in point_group_opearation if g in range(1, 33)])
        print(f"\n=== 生成结构{struct_idx + 1}，使用点群{point_group}，目标{TARGET_ATOMS}原子 ===")

        while len(pos_list) < TARGET_ATOMS:
            try:
                # 生成有效基础原子（NumPy数组）
                r = rand.uniform(*RADIUS_RANGE)
                base_pos = generate_valid_base(pos_list, r)
            except RuntimeError as e:
                print(f"警告：{e}，当前原子数{len(pos_list)}，提前终止")
                break

            # 应用点群操作并去重（返回NumPy数组）
            new_group: np.ndarray = apply_group_operations(base_pos, point_group)
            # 过滤与现有原子距离过近的新原子（所有坐标均为NumPy数组）
            valid_new = [
                pos for pos in new_group  # pos是NumPy数组
                if all(np.linalg.norm(pos - existing) >= MIN_DISTANCE for existing in pos_list)
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
                print(f"终止条件触发：添加{needed}原子（{current}→{current + needed}）")
                break
            else:
                pos_list.extend(valid_new)  # 扩展NumPy数组列表
                print(f"添加{new_count}原子，当前总数{current + new_count}")

        # 调整坐标到晶胞中心并保存（所有坐标均为NumPy数组）
        pos_array = np.array(pos_list) + center  # 数组运算自动对齐
        atoms = Atoms(
            symbols=['C'] * len(pos_array),
            positions=pos_array,
            cell=[CELL_SIZE] * 3,
            pbc=True
        )
        res_path = f"input/structure_{struct_idx + 1}.res"
        generate_res_file(res_path, atoms)
        print(f"结构{struct_idx + 1}保存完成，实际原子数{len(pos_array)}")
