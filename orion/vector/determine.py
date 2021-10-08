#! /usr/bin/env python3

import typing;
import numpy as np;

def factorial(x: int):
    if (x == 1): return 1;
    return x * factorial(x-1);


def _permute(array: np.array, d: typing.List[int] = [], r: int = 1):

    for x in range(array.size):
        if x in d: continue;
        if array.size == r:
            yield *(array[i] for i in d), array[x];
        else:
            for m in _permute(array, [*d, x], r + 1):
                yield m;

def _cr_is_even(a: int, b: int):

    return not (a%2)^(b%2);

def _cr_matrix_plus_minus_auto(array: np.array, row: int, column: int):

    return array[row][column] if _cr_is_even(row, column) else array[row][column] * -1;

def permute(array: np.array):

    return np.array([ x for x in _permute(array) ], dtype=array.dtype);
    
def inverse(array: np.array):

    t: int = 0;
    
    for (i, x) in enumerate(array):
        k: int = 0;
        for j in range(i, array.size):
            if x > array[j]:
                k = k + 1;
        print(x, '>', *array[i+1:], '=', k)
        t = t + k;

    print(t);

    return t, "odd" if t%2 else "even";

def sarrus_column_auto(array: np.array):

    ## debug
    array: np.array = np.array([*map(lambda x: [*map(lambda c: c.real, x)],array)], dtype=np.int64);

    print(array);

    shape: tuple = array.shape;
    rows: int = shape[0];
    columns: int = shape[1];

    R: np.array = np.array([ 1 for i in range(columns)], dtype=array.dtype);
    L: np.array = np.array([ 1 for i in range(columns)], dtype=array.dtype);

    if shape == (2, 2):
        R[0] = R[0] * array[0][0];
        R[0] = R[0] * array[1][1];
        R[1] = 0;
        L[0] = L[0] * array[0][1];
        L[0] = L[0] * array[1][0];
        L[1] = 0;
    else:
        for row in range(rows):
            for column in range(columns):

                p: int = (row + column) % columns;

                R[column] = R[column] * array[row][p];

                L[column] = L[column] * array[rows - row - 1][p];
    
    print(R, L);
    
    R: int = sum(R);
    L: int = sum(map(lambda x: -x, L));

    print(R, L);

    return R + L;

def cofactor_column_auto(array: np.array):

    ## debug
    array: np.array = np.array([*map(lambda x: [*map(lambda c: c.real, x)],array)], dtype=np.int64);

    print(array);

    shape: tuple = array.shape;
    rows: int = shape[0];
    columns: int = shape[1];

    choices: int = 0

    values: np.array = np.zeros([columns], dtype=array.dtype);
    temp: np.array = np.zeros([(rows - 1) * columns, columns - 1], dtype=array.dtype);

    t: int = temp.shape[0];
    s: int = temp.shape[1];

    for row in range(rows):

        if not choices:

            choices: int = 1;

            for column in range(columns):
                values[column] = _cr_matrix_plus_minus_auto(array, row, column);
                print(_cr_matrix_plus_minus_auto(array, row, column), end=" ");
            print();

            continue

        for column in range(columns):
            c: int = 0;
            for past in range(columns):
                if column == past: continue;
                r: int = (columns - 1) * column + row - 1;
                temp[r:r+1][0][c] = array[row][past];
                c: int = c + 1;

    for i in range(columns): ## t // s ## same as possible
        
        m: np.array = temp[i*s:i*s+s,0:s];
        
        print();
        
        sarr: int = sarrus_column_auto(m);

        print();
        
        print(m, sarr, "*", values[i], "=", sarr * values[i]);
        
        values[i] = values[i] * sarr;

    return sum(values);
