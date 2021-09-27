#! /usr/bin/env python3

import orion;
from orion.vector.concept_docs import *;

rotate_pos
switch_column_pos
switch_row_pos
mutate_column_pos
mutate_row_pos
revoke_column_pos
revoke_row_pos
rank_column_auto
rank_row_auto
# 
# m = np.array([
    # [1,2,3],
    # [4,5,6],
    # [7,8,9]
# ])
# 
# m = switch_row_pos(m, 0, 2)
# 
# m = mutate_row_pos(m, (1,2), (2,3))
# print(m)
# 
# m = revoke_row_pos(m, (1,2), (2,3))
# print(m)
# 
# m = switch_row_pos(m, 2, 1)
# print(m)
# 
# print(rank_column_auto(m))
# print(rank_row_auto(m))
# 
# print()

m = np.array([
    [4,2,-1],
    [3,0,2],
    [8,6,1]
])

print(1, m, end="\n\n")

print("H1 2")
print(switch_column_pos(m, 0, 1))

print("K1 3")
print(switch_row_pos(m, 0, 2))

print("H2^-2")
print(mutate_column_pos(m, (1, 0), (1, -2)))

print("K3^2")
print(mutate_row_pos(m, (2, 0), (2, 2)))

print("H3 1^1")
print(mutate_column_pos(m, (2, 1), (0, 1)))

print("K2 1^2")
print(mutate_row_pos(m, (1, 1), (0, 2)))

print("H2^1 3^2")
print(mutate_column_pos(m, (1, 1), (2, 2)))

print()

m = np.array([
    [4,2,-1],
    [3,0,2],
    [8,6,1]
])

print(2, m, end="\n\n")

print("H3 1^1")
print(revoke_column_pos(m, (2, 1), (0,1)))

print()

m = np.array([
    [2,3,1],
    [2,1,2],
    [4,4,3]
])

print(3, m, end="\n\n")

print(rank_column_auto(m))
