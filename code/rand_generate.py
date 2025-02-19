# 随机生成晶胞结构： n个原子，C/N/B/O

import numpy as np
from ase import Atoms

def generate_random_atoms(n: int, cell: np.ndarray, pbc: bool = True) -> Atoms :
    rand = np.random.default_rng()
    symbols = rand.choice(['C', 'N', 'B', 'O'], size=n)

    # 生成分数坐标
    scaled_positions = rand.random(size=(n, 3))

    # 生成实际坐标
    certain_positions = np.dot(scaled_positions, cell)

    # 生成原子结构
    atoms = Atoms(
        symbols=symbols,
        positions=certain_positions,
        cell=cell,
        pbc=pbc
    )
    return atoms

