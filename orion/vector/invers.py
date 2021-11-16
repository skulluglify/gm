#! /usr/bin/env python3

import  typing;
import numpy as np;
from vector.concept_docs \
import *;
from vector.determine \
import *;
from vector.minor \
import *;

def multiple_matrix(A: np.array, B: np.array):

    ## debug
    A: np.array = np.array([*map(lambda x: [*map(lambda c: c.real, x)],A)], dtype=np.int64);
    B: np.array = np.array([*map(lambda x: [*map(lambda c: c.real, x)],B)], dtype=np.int64);

    print(A);
    print(B);

    ## transpose B
    B: np.array = transpose(B.copy());

    shapeA: typing.Tuple = A.shape;
    rowsA: int = shapeA[0];
    columnsA: int = shapeA[1];

    shapeB: typing.Tuple = B.shape;
    rowsB: int = shapeB[0];
    columnsB: int = shapeB[1];
    
    rows = rowsA if rowsA < rowsB else rowsB;
    columns = columnsA if columnsA < columnsB else columnsB;

    ## caches using high data typing
    # caches: np.array = np.zeros((rows, columns), dtype=np.complex64);

    ## caches for debugging
    caches: np.array = np.zeros((rows, columns), dtype=np.int64);

    for row in range(rows):
        for column in range(columns):
            
            caches[row][column] = sum(A[row] * B[column]);

    return caches;


def invers(array: np.array):

    ## debug
    array: np.array = np.array([*map(lambda x: [*map(lambda c: c.real, x)],array)], dtype=np.int64);

    print(array);

    shape: typing.Tuple = array.shape;
    rows: int = shape[0];
    columns: int = shape[1];

    caches: np.array = np.zeros(shape, dtype=array.dtype);

    for row in range(rows):
        for column in range(columns):

            value = array[row][column];
            value = value if not (row % 2)^(column % 2) else value * -1;
            caches[row][column] = value;
    
    print(caches);

    return caches;

def invers_matrix_ordo_2x2 (array: np.array):

    ## debug
    array: np.array = np.array([*map(lambda x: [*map(lambda c: c.real, x)],array)], dtype=np.int64);

    print(array);

    shape: typing.Tuple = array.shape;
    rows: int = shape[0];
    columns: int = shape[1];

    caches: np.array = np.zeros(shape, dtype=array.dtype);

    s: int = sarrus_column_auto(array);

    print(end="\n\n");

    print("1 /", s, end="\n\n");
    print(array, end="\n\n");

    s: int = 1 / s;

    a: int = array[0][0];
    b: int = array[0][1];
    c: int = array[1][0];
    d: int = array[1][1];

    array[0][0] = d;
    array[0][1] = b * -1;
    array[1][0] = c * -1;
    array[1][1] = a;

    for row in range(rows):

        for column in range(columns):

            caches[row][column] = s * array[row][column];
    
    return caches;

def invers_matrix_ordo_3x3 (array: np.array):

    ## debug
    array: np.array = np.array([*map(lambda x: [*map(lambda c: c.real, x)],array)], dtype=np.int64);

    print(array);

    shape: typing.Tuple = array.shape;
    rows: int = shape[0];
    columns: int = shape[1];

    caches: np.array = np.zeros(shape, dtype=array.dtype);

    d: int = cofactor_column_auto(array);

    print(d);

    if (d != 0):

        print("array have inversion");

        adjoint: np.array = adjoint_matrix(array);

        for row in range(rows):

            for column in range(columns):

                caches[row][column] = d * adjoint[row][column];
    
    return caches;

# def invers_elementer_ordo_2x2 (array: np.array):

#     ## debug
#     array: np.array = np.array([*map(lambda x: [*map(lambda c: c.real, x)],array)], dtype=np.int64);

#     print(array);

#     shape: typing.Tuple = array.shape;
#     rows: int = shape[0];
#     columns: int = shape[1];

#     shadow: np.array = np.array([
#         [1, 0],
#         [0, 1]
#     ], dtype=array.dtype);

#     caches: np.array = shadow.copy();

#     for row in range(rows):

#         for column in range(columns):

#             a: int = array[row][column];
#             s: int = shadow[row][column];

#             if (s != 0):
                
#                 v: int = s / a;
#                 array[row] = array[row] * v;
#                 shadow[row] = shadow[row] * v;
            
#             else:

#                 for r in range(row, rows):

#                     c: int = array[r][column];
#                     d: int = caches[r][column];

#                     e: int = c - d;
#                     e: int = e / a;

#                     ## aaaarghhh
