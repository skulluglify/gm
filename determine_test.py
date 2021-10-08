#! /usr/bin/env python3 

import orion;
from orion.vector.determine import *;
import orion.vector.concept;

a: np.array = np.array([
    1, 2, 3
], dtype=np.uint32);

print(permute(a));

b: np.array = np.array([
    6, 4, 5, 3, 1, 2
], dtype=np.uint32);


# 6 > 4 5 3 1 2 > 5
# 4 > 5 3 1 2 > 3
# 5 > 3 1 2 > 3
# 3 >  1 2 > 2
# 1 > 2 > 0
print(inverse(b));

# a: np.array = np.array([
    # [2, 7],
    # [4, 5]
# ], dtype=np.uint32);

a: np.array = np.array([
    [1, 2, 3],
    [-4, 5, 6],
    [7, -8, 9]
], dtype=np.complex64);

print(sarrus_column_auto(orion.vector.concept.rotate_pos(a)));

a: np.array = np.array([
    [2, 1, 6, 7],
    [3, 2, 4, 5],
    [4, 4, 2, 3],
    [5, 6, 1, 4]
], dtype=np.complex64);

# a: np.array = np.array([
#     [3, 2, 5],
#     [4, 6, 7],
#     [2, 9, 2]
# ], dtype=np.complex64);

print(cofactor_column_auto(a));
