
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

restricoesIgualCoef = np.array([[1,1,1]])
restricoesIgualResult = np.array([999])
restricoesMenorCoef = np.array([
[1, 4, 8],
[40,30,20],
[3,2,4]])
restricoesMenorResult = np.array([4500, 36000,2700])
custo = np.array([70, 80, 85])

res = linprog(custo, A_eq=restricoesIgualCoef, b_eq=restricoesIgualResult, A_ub=restricoesMenorCoef, b_ub=restricoesMenorResult,
bounds=(0, None))
print('Solução ótima:', res.fun, '\nX:', res.x)