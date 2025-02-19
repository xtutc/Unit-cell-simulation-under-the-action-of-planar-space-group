# 六方晶系引用

import numpy as np

# 定义参数
rand = np.random.default_rng()
a, c = 20*rand.random(size=2)
b=a
# gamma a与b之间的夹角
# beta a与c之间的夹角
# alpha b与c之间的夹角
gamma, beta, alpha = 120, 90, 90
alpha = np.radians(alpha)
beta = np.radians(beta)
gamma = np.radians(gamma)
print(f"a = {a}, b = {b}, c = {c}, alpha = {alpha}, beta = {beta}, gamma = {gamma}")


# 初始化坐标
x0 = [a, b, c, alpha, beta, gamma]

# 定义六方矩阵，方便主函数调用，生成原子坐标（笛卡尔坐标）
h = np.sqrt(1 - np.cos(gamma)**2)
hexagonal_cell = np.array([[a, 0, 0],
                 [b*np.cos(gamma), b*np.sin(gamma), 0],
                 [c * np.cos(beta), c * (np.cos(alpha) - np.cos(beta) * np.cos(gamma)) / np.sin(gamma), c*h]])
