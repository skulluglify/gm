#! /usr/bin/env python3

import orion;
from orion.vector.concept_docs \
import *;
from orion.vector.determine \
import *;
from orion.vector.minor \
import *;

print("EXAM 1")

A: np.array = np.array([

    [ 1,  3,  5],
    [ 2,  4,  6], 
    [-1,  8,  2]
])

R: np.array = adjoint_matrix(A);

print(end="\n\n");

print(R);

print("END", end="\n\n")


print("EXAM 2 A")

A: np.array = np.array([

    [ 0,  6,  0],
    [ 8,  6,  8], 
    [ 3,  2,  2]
])

R: int = sarrus_column_auto(A);

print(end="\n\n");

print(R);

print("END", end="\n\n")


print("EXAM 2 B")

R: int = cofactor_column_auto(A);

print(end="\n\n");

print(R);

print("END", end="\n\n")

print("EXAM 3")

A: np.array = np.array([
    [ 3,  4,  4],
    [ 3,  6, -1],
    [ 1, -2,  2]
], dtype=np.int64);

print(rank_column_auto(A))

print("END", end="\n\n")

print("EXAM 4 A")

A: np.array = np.array([

    [ 3,  1,  4],
    [ 2,  1,  1], 
    [ 3,  0,  1]
])

R: int = switch_row_pos(A, 1, 0);

print(end="\n\n");

print(R);

print("END", end="\n\n")

print("EXAM 4 B")

R: int = switch_column_pos(A, 0, 1);

print(end="\n\n");

print(R);

print("END", end="\n\n")

print("EXAM 4 C")

R: int = switch_column_pos(A, 1, 2);

print(end="\n\n");

print(R);

print("END", end="\n\n")

print("EXAM 4 D")

R: int = mutate_row_pos(A, (1, 1), (0, 2));

print(end="\n\n");

print(R);

print("END", end="\n\n")
