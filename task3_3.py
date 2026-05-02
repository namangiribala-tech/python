import numpy as np
import math
from itertools import combinations
from scipy.special import comb


#(i) Matrix Operations

# Row sums
print("Row sums:", np.sum(O, axis=1))

# Column sums
print("Column sums:", np.sum(O, axis=0))

# Mean & std
means = np.mean(O, axis=0)
stds = np.std(O, axis=0)

print("Means:", means)
print("Std Dev:", stds)

# Highest average category
categories = ['E', 'C', 'B', 'G']
print("Highest avg category:", categories[np.argmax(means)])

#(ii) Solve Linear System
#x2 - 1.5x3 = 0
#0.6x1 - 0.4x2 - 0.4x3 = 0
#x1 + x2 + x3 = 500000

A = np.array([
    [0, 1, -1.5],
    [0.6, -0.4, -0.4],
    [1, 1, 1]
])

b = np.array([0, 0, 500000])

solution = np.linalg.solve(A, b)

print("Solution (x1, x2, x3):", solution)

# Residual
residual = np.linalg.norm(np.dot(A, solution) - b)
print("Residual:", residual)

# Determinant
det = np.linalg.det(A)
print("Determinant:", det)