#! /usr/bin/env python3

import orion;
from orion.vector.invers \
import *;

B: np.array = np.array([
    [ 2, 1 ], 
    [ 3, 2 ]
])

A = B.copy();
B = invers(B);

C: np.array = multiple_matrix(A, B);
S: int = sarrus_column_auto(C);

print(end="\n\n");
print(C, end="\n\n");
print(S);
print("Singular" if not S else "Tidak Singular");


print("END", end="\n\n");

A: np.array = np.array([
    [ 4, 1 ], 
    [ 7, 2 ]
]);

print(invers_matrix_ordo_2x2(A));

print("END", end="\n\n");

A: np.array = np.array([
    [ 1, 2, 1],
    [ 0, 3, 1],
    [-1, 2, 0]
])

print(invers_matrix_ordo_3x3(A));

A: np.array = np.array([
    [ 1, 2, 3],
    [ 2, 5, 3],
    [ 1, 0, 8]
])

print(invers_matrix_ordo_3x3(A));