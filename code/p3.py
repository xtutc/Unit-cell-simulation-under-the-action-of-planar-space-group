import numpy as np
from ase import Atoms
import random
from merge_close import merge_close_atoms

# 定义 p3 平面群的所有对称操作（旋转矩阵和平移向量）
p3_operations = [
    # 1. 恒等操作
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 'translation': np.array([0, 0, 0])},
    # 2. (x → -y) + (y → x-y)
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, 1]]), 'translation': np.array([0, 0, 0])},
    # 3. (x → -x+y) + (y → -x)
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, 1]]), 'translation': np.array([0, 0, 0])},
]

def p3_generate_atoms_structure(cell: np.ndarray,
                                  scale_position: np.ndarray,
                                  min_distance: float,
                                  symbol_rule: str):

    n = len(scale_position)
    new_scale_position = np.zeros_like(scale_position)

    # 对每个原子随机挑选一个对称操作进行应用
    for i in range(n):
        op = random.choice(p3_operations)
        R = op['rotation']
        t = op['translation']
        # 应用旋转和平移
        transformed = np.dot(scale_position[i], R) + t
        # 处理周期性边界条件
        new_scale_position[i] = transformed % 1.0

    # 将分数坐标转换为笛卡尔坐标
    new_position = np.dot(new_scale_position, cell)
    old_position = np.dot(scale_position, cell)

    # 随机生成元素符号
    rand = np.random.default_rng()
    old_symbols = rand.choice(['C', 'N', 'O', 'B'], size=n)
    new_symbols = rand.choice(['C', 'N', 'O', 'B'], size=n)

    # 合并新旧原子
    all_symbols = np.concatenate((old_symbols, new_symbols))
    all_positions = np.concatenate((old_position, new_position))

    # 创建原子结构
    atoms = Atoms(
        symbols=all_symbols,
        positions=all_positions,
        cell=cell,
        pbc=True
    )

    # 合并邻近原子
    merge_atoms = merge_close_atoms(atoms, min_distance, symbol_rule)

    return merge_atoms
