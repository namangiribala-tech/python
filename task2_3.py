import numpy as np
import math
from itertools import combinations
from scipy.special import comb


O = np.array([
    [40, 25, 15, 30],
    [20, 35, 10, 45],
    [50, 20, 30, 20],
    [15, 40, 20, 25],
    [35, 15, 25, 10]
])

#Basic Probabilities
total_records = O.size  # 20

# P(W3)
P_W3 = 4 / total_records

# P(order > 30)
count_gt_30 = np.sum(O > 30)
P_gt_30 = count_gt_30 / total_records

print("P(W3):", P_W3)
print("P(order > 30):", P_gt_30)

#A ∪ B
# A = W2
A_count = 4
P_A = A_count / total_records

# B = order > 30
P_B = P_gt_30

# A ∩ B
W2 = O[1]
A_intersection_B = np.sum(W2 > 30) / total_records

# A ∪ B
P_union = P_A + P_B - A_intersection_B

print("P(A):", P_A)
print("P(B):", P_B)
print("P(A ∩ B):", A_intersection_B)
print("P(A ∪ B):", P_union)

