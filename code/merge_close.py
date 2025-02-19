from ase import Atoms
import numpy as np
from scipy.spatial.distance import cdist


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  # 用于按秩合并

    def find(self, x):
        if self.parent[x] != x:
            # 路径压缩
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # 按秩合并
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


def merge_close_atoms(atoms: Atoms,
                      min_distance: float,
                      symbol_rule: str):
    positions = atoms.positions  # 从 atoms 中获取位置
    cell = atoms.cell  # 获取晶胞
    symbols = atoms.get_chemical_symbols()  # 获取元素符号
    pbc = atoms.pbc  # 获取周期性边界条件

    n = len(positions)

    # 检查 cell 和 pbc 的有效性
    cell = np.asarray(cell)
    pbc = np.asarray(pbc, dtype=bool)

    if len(pbc) != 3:
        raise ValueError("pbc 必须是长度为 3 的数组。")

    if np.any(np.isnan(cell)) or np.any(np.isnan(pbc)):
        raise ValueError("cell 或 pbc 存在无效值。")

    # 创建并查集用于合并
    uf = UnionFind(n)

    # 计算距离矩阵，考虑周期性边界条件
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            # 计算坐标差值
            diff = positions[i] - positions[j]
            # 周期性边界处理
            for k in range(3):  # 处理每个方向
                if pbc[k]:
                    if cell[k, k] != 0:  # 确保 cell[k] 不是零
                        # 如果周期性边界，检查距离是否超过一半晶胞大小
                        diff[k] -= np.round(diff[k] / cell[k, k]) * cell[k, k]
            dist = np.linalg.norm(diff)  # 计算修正后的距离
            distance_matrix[i, j] = dist
            distance_matrix[j, i] = dist

    # 判断哪些原子需要合并
    for i in range(n):
        for j in range(i + 1, n):
            if distance_matrix[i, j] < min_distance:
                uf.union(i, j)

    # 根据并查集结果合并原子
    groups = {}
    for i in range(n):
        root = uf.find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)

    # 如果没有需要合并的组，提前退出
    if all(len(g) == 1 for g in groups.values()):
        return atoms

    # 生成新的原子位置和种类
    # 生成新的原子位置和种类
    new_symbols = []
    new_positions = []

    # 合并原子
    for group in groups.values():
        if len(group) == 1:
            # 只有一个原子，不需要合并
            idx = group[0]
            new_positions.append(positions[idx])
            new_symbols.append(symbols[idx])
        else:
            # 计算质心位置
            merged_pos = np.mean(positions[group], axis=0)
            new_positions.append(merged_pos)

            # 确定合并后的原子种类
            if symbol_rule == 'first':
                merged_sym = symbols[group[0]]  # 取第一个原子的种类
            elif symbol_rule == 'random':
                merged_sym = np.random.choice([symbols[i] for i in group])  # 随机选择一个种类
            elif symbol_rule == 'majority':
                from collections import defaultdict
                count = defaultdict(int)
                for idx in group:
                    count[symbols[idx]] += 1
                merged_sym = max(count, key=lambda k: count[k])
            else:
                raise ValueError(f"Unsupported symbol_rule: {symbol_rule}")
            new_symbols.append(merged_sym)

    # 确保 positions 和 symbols 长度一致
    print(f"Number of new positions: {len(new_positions)}")
    print(f"Number of new symbols: {len(new_symbols)}")

    # 更新 Atoms 对象
    current_atoms = Atoms(
        symbols=new_symbols,
        positions=new_positions,
        cell=cell,
        pbc=pbc
    )
