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

class concept (object):

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

        shape: tuple = array.shape;
        rows: int = shape[0];
        columns: int = shape[1];

        R: np.array = np.array([ 1 for i in range(columns)], dtype=array.dtype);
        L: np.array = np.array([ 1 for i in range(columns)], dtype=array.dtype);

        for row in range(rows):
            for column in range(columns):
                p: int = column;

                # c: int = (row + column) % columns;
                column: int = (row + column) % columns;
                # R[p] = R[p] * array[row][c];
                R[p] = R[p] * array[row][column];

                # c: int = (row + column) % columns;
                # L[p] = L[p] * array[rows - row - 1][c];
                L[p] = L[p] * array[rows - row - 1][column];

        R: int = sum(R);
        L: int = sum(map(lambda x: -x, L));

        return R + L;