import numpy as np


rand = np.random.default_rng()
# 定义参数，随机生成晶轴长度 a, b, c，范围在 0 到 10 之间
rand = np.random.default_rng()
a, b, c = 20 * rand.random(size=3)

# 矩形晶系中，a 与 b、a 与 c、b 与 c 之间的夹角均为 90 度，直接使用弧度制
alpha = beta = gamma = np.radians(90)

# 打印生成的晶轴长度和夹角
print(f"a = {a}, b = {b}, c = {c}, alpha = {alpha}, beta = {beta}, gamma = {gamma}")

# 定义矩形矩阵，方便主函数调用，生成原子坐标（笛卡尔坐标）
h = np.sqrt(1 - np.cos(gamma) ** 2)
rectangular_cell = np.array([[a, 0, 0],
                            [b * np.cos(gamma), b * np.sin(gamma), 0],
                            [c * np.cos(beta), c * (np.cos(alpha) - np.cos(beta) * np.cos(gamma)) / np.sin(gamma),c * h]])