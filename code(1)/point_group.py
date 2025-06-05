import numpy as np


c1_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
]

c2_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])},
]

c2h_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])},
]

c2v_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])},
]

c3_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, 1]])},
]

c3h_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, -1]])},
]

c3i_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, -1, 0], [1, 0, 0], [0, 0, -1]])},
]

c3v_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 1, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, 0, 0], [1, -1, 0], [0, 0, 1]])},
]

c4_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])},
]

c4h_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [1, 0, 0], [0, 0, -1]])},
]

c4v_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])},
]

c6_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, -1, 0], [1, 0, 0], [0, 0, 1]])},
]

c6h_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, -1, 0], [1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, -1, 0], [1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, -1]])},
]

c6v_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, -1, 0], [1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 1, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, 0, 0], [1, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, -1, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [-1, 1, 0], [0, 0, 1]])},
]

ci_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])},
]

cs_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])},
]

d2_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]])},
]

d2d_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])},
]

d2h_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])},
]

d3_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 1, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [1, -1, 0], [0, 0, -1]])},
]

d3d_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 1, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [1, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, -1, 0], [1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, -1, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [-1, 1, 0], [0, 0, 1]])},
]

d3h_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 1, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, 0, 0], [1, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 1, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [1, -1, 0], [0, 0, -1]])},
]

d4_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])}
]

d4h_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])},
]

d6_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, -1, 0], [1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, -1, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 0, 0], [-1, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 1, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [1, -1, 0], [0, 0, -1]])},
]

d6h_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, -1, 0], [1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, -1, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 0, 0], [-1, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 1, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [1, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, -1, 0], [1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [1, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 1, 0], [-1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 1, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, 0, 0], [1, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, -1, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [-1, 1, 0], [0, 0, 1]])},
]

o_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])},
    {'rotation': np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]])},
    {'rotation': np.array([[0, 0, -1], [-1, 0, 0], [0, 1, 0]])},
    {'rotation': np.array([[0, 0, -1], [1, 0, 0], [0, -1, 0]])},
    {'rotation': np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])},
    {'rotation': np.array([[0, -1, 0], [0, 0, 1], [-1, 0, 0]])},
    {'rotation': np.array([[0, 1, 0], [0, 0, -1], [-1, 0, 0]])},
    {'rotation': np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]])},
    {'rotation': np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])},
    {'rotation': np.array([[-1, 0, 0], [0, 0, 1], [0, 1, 0]])},
    {'rotation': np.array([[-1, 0, 0], [0, 0, -1], [0, -1, 0]])},
    {'rotation': np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])},
    {'rotation': np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])},
    {'rotation': np.array([[0, 0, 1], [0, -1, 0], [1, 0, 0]])},
    {'rotation': np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]])},
    {'rotation': np.array([[0, 0, -1], [0, -1, 0], [-1, 0, 0]])},
]

oh_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])},
    {'rotation': np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]])},
    {'rotation': np.array([[0, 0, -1], [-1, 0, 0], [0, 1, 0]])},
    {'rotation': np.array([[0, 0, -1], [1, 0, 0], [0, -1, 0]])},
    {'rotation': np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])},
    {'rotation': np.array([[0, -1, 0], [0, 0, 1], [-1, 0, 0]])},
    {'rotation': np.array([[0, 1, 0], [0, 0, -1], [-1, 0, 0]])},
    {'rotation': np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]])},
    {'rotation': np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])},
    {'rotation': np.array([[-1, 0, 0], [0, 0, 1], [0, 1, 0]])},
    {'rotation': np.array([[-1, 0, 0], [0, 0, -1], [0, -1, 0]])},
    {'rotation': np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])},
    {'rotation': np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])},
    {'rotation': np.array([[0, 0, 1], [0, -1, 0], [1, 0, 0]])},
    {'rotation': np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]])},
    {'rotation': np.array([[0, 0, -1], [0, -1, 0], [-1, 0, 0]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 0, -1], [-1, 0, 0], [0, -1, 0]])},
    {'rotation': np.array([[0, 0, -1], [1, 0, 0], [0, 1, 0]])},
    {'rotation': np.array([[0, 0, 1], [1, 0, 0], [0, -1, 0]])},
    {'rotation': np.array([[0, 0, 1], [-1, 0, 0], [0, 1, 0]])},
    {'rotation': np.array([[0, -1, 0], [0, 0, -1], [-1, 0, 0]])},
    {'rotation': np.array([[0, 1, 0], [0, 0, -1], [1, 0, 0]])},
    {'rotation': np.array([[0, -1, 0], [0, 0, 1], [1, 0, 0]])},
    {'rotation': np.array([[0, 1, 0], [0, 0, 1], [-1, 0, 0]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 0, -1], [0, 1, 0]])},
    {'rotation': np.array([[1, 0, 0], [0, 0, -1], [0, -1, 0]])},
    {'rotation': np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])},
    {'rotation': np.array([[-1, 0, 0], [0, 0, 1], [0, -1, 0]])},
    {'rotation': np.array([[0, 0, -1], [0, -1, 0], [1, 0, 0]])},
    {'rotation': np.array([[0, 0, -1], [0, 1, 0], [-1, 0, 0]])},
    {'rotation': np.array([[0, 0, 1], [0, -1, 0], [-1, 0, 0]])},
    {'rotation': np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])},

]

s4_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [1, 0, 0], [0, 0, -1]])},
]

t_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])},
    {'rotation': np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]])},
    {'rotation': np.array([[0, 0, -1], [-1, 0, 0], [0, 1, 0]])},
    {'rotation': np.array([[0, 0, -1], [1, 0, 0], [0, -1, 0]])},
    {'rotation': np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])},
    {'rotation': np.array([[0, -1, 0], [0, 0, 1], [-1, 0, 0]])},
    {'rotation': np.array([[0, 1, 0], [0, 0, -1], [-1, 0, 0]])},
    {'rotation': np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]])},

]

td_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])},
    {'rotation': np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]])},
    {'rotation': np.array([[0, 0, -1], [-1, 0, 0], [0, 1, 0]])},
    {'rotation': np.array([[0, 0, -1], [1, 0, 0], [0, -1, 0]])},
    {'rotation': np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])},
    {'rotation': np.array([[0, -1, 0], [0, 0, 1], [-1, 0, 0]])},
    {'rotation': np.array([[0, 1, 0], [0, 0, -1], [-1, 0, 0]])},
    {'rotation': np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]])},
    {'rotation': np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, -1, 0], [-1, 0, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 1, 0], [-1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, -1, 0], [1, 0, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])},
    {'rotation': np.array([[-1, 0, 0], [0, 0, 1], [0, -1, 0]])},
    {'rotation': np.array([[-1, 0, 0], [0, 0, -1], [0, 1, 0]])},
    {'rotation': np.array([[1, 0, 0], [0, 0, -1], [0, -1, 0]])},
    {'rotation': np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])},
    {'rotation': np.array([[0, 0, 1], [0, -1, 0], [-1, 0, 0]])},
    {'rotation': np.array([[0, 0, -1], [0, 1, 0], [-1, 0, 0]])},
    {'rotation': np.array([[0, 0, -1], [0, -1, 0], [1, 0, 0]])},
]

th_operations=[
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])},
    {'rotation': np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]])},
    {'rotation': np.array([[0, 0, 1], [-1, 0, 0], [0, 1, 0]])},
    {'rotation': np.array([[0, 0, -1], [1, 0, 0], [0, -1, 0]])},
    {'rotation': np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])},
    {'rotation': np.array([[0, -1, 0], [0, 0, 1], [-1, 0, 0]])},
    {'rotation': np.array([[0, 1, 0], [0, 0, -1], [-1, 0, 0]])},
    {'rotation': np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]])},
    {'rotation': np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])},
    {'rotation': np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])},
    {'rotation': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])},
    {'rotation': np.array([[0, 0, -1], [-1, 0, 0], [0, -1, 0]])},
    {'rotation': np.array([[0, 0, -1], [1, 0, 0], [0, 1, 0]])},
    {'rotation': np.array([[0, 0, 1], [1, 0, 0], [0, -1, 0]])},
    {'rotation': np.array([[0, 0, 1], [-1, 0, 0], [0, 1, 0]])},
    {'rotation': np.array([[0, -1, 0], [0, 0, -1], [-1, 0, 0]])},
    {'rotation': np.array([[0, 1, 0], [0, 0, -1], [1, 0, 0]])},
    {'rotation': np.array([[0, -1, 0], [0, 0, 1], [1, 0, 0]])},
    {'rotation': np.array([[0, -1, 0], [0, 0, 1], [-1, 0, 0]])},
]


# 空间群对应的原子生成函数
point_group_opearation= {
    1: c1_operations,
    2: c2_operations,
    3: c2h_operations,
    4: c2v_operations,
    5: c3_operations,
    6: c3h_operations,
    7: c3i_operations,
    8: c3v_operations,
    9: c4_operations,
    10: c4h_operations,
    11: c4v_operations,
    12: c6_operations,
    13: c6h_operations,
    14: c6v_operations,
    15: ci_operations,
    16: cs_operations,
    17: d2_operations,
    18: d2d_operations,
    19: d2h_operations,
    20: d3_operations,
    21: d3d_operations,
    22: d3h_operations,
    23: d4_operations,
    24: d4h_operations,
    25: d6_operations,
    26: d6h_operations,
    27: o_operations,
    28: oh_operations,
    29: s4_operations,
    30: t_operations,
    31: td_operations,
    32: th_operations,
}


