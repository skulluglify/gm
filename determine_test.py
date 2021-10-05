#! /usr/bin/env python3 

import orion;
from orion.vector.determine import *;
import orion.vector.concept;

a: np.array = np.array([
    1, 2, 3
], dtype=np.uint32);

print(concept.permute(a));

b: np.array = np.array([
    6, 4, 5, 3, 1, 2
], dtype=np.uint32);


# 6 > 4 5 3 1 2 > 5
# 4 > 5 3 1 2 > 3
# 5 > 3 1 2 > 3
# 3 >  1 2 > 2
# 1 > 2 > 0
print(concept.inverse(b));

# a: np.array = np.array([
    # [2, 7],
    # [4, 5]
# ], dtype=np.uint32);

a: np.array = np.array([
    [1, 2, 3],
    [-4, 5, 6],
    [7, -8, 9]
], dtype=np.complex64);

print(concept.sarrus_column_auto(orion.vector.concept.rotate_pos(a)));
