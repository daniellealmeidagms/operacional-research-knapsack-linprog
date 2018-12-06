import numpy as np
from scipy.optimize import linprog
from numpy.linalg import solve

"""
minimize f(x) = 70x_1 + 80x_2 + 85x_3 
x_1 + x_2 + x_3 = 999
x_1 + 4x_2 + 8x_3 <= 4500
40x_1 + 30x_2 + 20x_3 <= 36000
3x_1 + 2x_2 + 4x_3 <= 2700
x_1, x_2, x_3 >= 0

"""

A = np.array([
[1, 1, 1, 0, 0, 0],
[1, 4, 8, 1, 0, 0],
[40, 30, 20, 0, 1, 0],
[3, 2, 4, 0, 0, 1]])

b = np.array([999, 4500, 36000, 2700])
c = np.array([70, 80, 85, 0, 0, 0])

res = linprog(c, A_eq=A, b_eq=b, bounds=(0, None))
print('Optimal value:', res.fun, '\nX:', res.x)