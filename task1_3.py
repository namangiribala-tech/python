import numpy as np
import math
from itertools import combinations
from scipy.special import comb



#Total Order Combinations
categories = 4
warehouses = 5
zones = 3

total_combinations = categories * warehouses * zones
print("Total order combinations:", total_combinations)




#Selecting 2 Categories
categories_list = ['E', 'C', 'B', 'G']

# (a)
print("Ways to select 2 categories:", comb(4, 2))

# (b) Electronics must be included
with_E = [c for c in combinations(categories_list, 2) if 'E' in c]
print("With Electronics:", len(with_E))

# (c) Electronics not included
without_E = [c for c in combinations(categories_list, 2) if 'E' not in c]
print("Without Electronics:", len(without_E))





#Non-empty subsets
subsets = []
for i in range(1, 5):
    subsets.extend(combinations(categories_list, i))

print("Total non-empty subsets:", len(subsets))
print("Subsets:", subsets)


#Permutations P(8,3)
perm_value = math.perm(8, 3)
print("P(8,3):", perm_value)

#Seating Arrangements
row = math.factorial(5)
circle = math.factorial(4)

print("Row arrangements:", row)
print("Circular arrangements:", circle)

