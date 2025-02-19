from ase import Atoms
import numpy as np
from ase.geometry import get_distances


# 定义并查集
class UnionFind:
    # 初始化节点
    def __int__(self, size):
        self.parent = list(range(size))

    # 路径压缩
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    # 合并集合
    def union(self, x, y):
        fx = self.find(self, x)
        fy = self.find(self, y)
        if fx != fy:
            self.parent[fy] = fx

# 空间群作用下的原子结构
def generate_atoms_structure(A:np.ndarray,
                             cell:np.ndarray,
                             n:int,
                             scale_position:np.ndarray,
                             min_distance:float,
                             symbol_rule:str):

    # 生成新的原子位置坐标
    new_scale_position = np.zeros(size=[n, 3])
    for i in range(n):
        new_scale_position[i, :] =  scale_position[i, :] @ A
    new_scale_position += scale_position
    new_position = np.dot(new_scale_position, cell)

    # 对每个点进行标记——随机生成元素
    rand = np.random.default_rng()
    symbols = rand.choice(['C', 'N', 'O', 'B'], size=n)

    #生成原子结构
    atoms = Atoms(
        symbols=symbols,
        positions=new_position,
        cell=cell,
        pbc=True
    )

    # 检查合并
    merge_atoms = merge_close_atoms(atoms. atoms, min_distance, symbol_rule)

    return merge_atoms

# 如何实现合并相邻元素结构
def merge_close_atoms(atoms:Atoms,
                      min_distance:float,
                      symbol_rule:str):
    current_atoms = atoms.copy()
    max_iter = 10
    for _ in range(max_iter):
        positions = current_atoms.get_positions()
        cell = current_atoms.get_cell()
        symbols = current_atoms.get_chemical_symbols()
        pbc = current_atoms.get_pbc()
        n = len(positions)

        # 使用并查集判断是否需要合并
        uf = UnionFind(n)
        distance = get_distances(positions, cell, pbc)[0]
        for i in range(n):
            for j in range(i+1, n):
                if distance[i, j] < min_distance:
                    uf.union(i, j)

        # 分组原子
        groups = { }
        for i in range(n):
            root = uf.find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)

        # 如果没有需要合并的组，提前退出
        if(all(len(g) == 1 for g in groups)):
            break

        # 生成新的原子位置和种类
        new_symbols = []
        new_positions = []
        for group in groups.values():
            # 如果组中只有一个，直接添加
            if len(group) == 1:
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
                    merged_sym = np.random.choice(symbols[group])  # 随机选择一个种类
                elif symbol_rule == 'majority':
                    # 统计出现次数最多的种类
                    from collections import defaultdict
                    count = defaultdict(int)
                    for idx in group:
                        count[symbols[idx]] += 1
                    merged_sym = max(count, key=lambda k: count[k])
                else:
                    raise ValueError(f"Unsupported symbol_rule: {symbol_rule}")
                new_symbols.append(merged_sym)

                # 更新 Atoms 对象
            current_atoms = Atoms(
                symbols=new_symbols,
                positions=new_positions,
                cell=cell,
                pbc=True
            )

            return current_atoms



