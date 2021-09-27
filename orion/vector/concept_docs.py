#! /usr/bin/env python3

import typing;
import numpy as np;

def _print_array_complex(array: np.array, *args, **kwargs):
    arraycopy: np.array = np.zeros(array.shape, dtype=np.float128);
    for row in range(array.shape[0]):
        for column in range(array.shape[1]):
            m: any = array[row][column];
            if isinstance(m, np.complex64):
                arraycopy[row][column] = round(m.real, 2);
            else:
                arraycopy[row][column] = round(m, 2);
    print(arraycopy, *args, **kwargs);

def _zip(array: np.array) -> np.array:
    row: int;
    column: int;
    shape: tuple = tuple( array.shape[i-1] for i in range(len(array.shape),0,-1) );
    arrayzeros: np.array = np.zeros([*shape], dtype=array.dtype);
    for row in range(shape[0]):
        for column in range(shape[1]):
            arrayzeros[row][column] = array[column][row];
    return arrayzeros;

def rotate_pos(array: np.array) -> np.array:
    return _zip(array);

def switch_column_pos(array: np.array, a: int, b: int) -> np.array:
    arraycopy: np.array = array.copy();
    arraycopy[a], arraycopy[b] = array[b], array[a];
    return arraycopy;

def switch_row_pos(array: np.array, a: int, b: int) -> np.array:
    return rotate_pos(switch_column_pos(rotate_pos(array), a, b));

def mutate_column_pos(array: np.array, a: tuple, b: tuple) -> np.array:
    arraycopy: np.array = array.copy();
    after: typing.Iterator = iter([*a, *a]);
    before: typing.Iterator = iter([*b, *b]);
    a: np.array = array[next(after)] * next(after);
    b: np.array = array[next(before)] * next(before);
    arraycopy[next(after)] = a + b;
    return arraycopy;

def mutate_row_pos(array: np.array, a: tuple, b: tuple) -> np.array:
    return rotate_pos(mutate_column_pos(rotate_pos(array), a, b));

def revoke_column_pos(array: np.array, a: tuple, b: tuple) -> np.array:
    arraycopy: np.array = array.copy();
    after: typing.Iterator = iter([*a, *a]);
    before: typing.Iterator = iter([*b, *b]);
    m: np.array = array[next(after)];
    b: np.array = array[next(before)] * next(before);
    m: np.array = (m - b) / next(after);
    arraycopy[next(after)] = m;
    return arraycopy;

def revoke_row_pos(array: np.array, a: tuple, b: tuple) -> np.array:
    return rotate_pos(revoke_column_pos(rotate_pos(array), a, b));

def get_pivot(array: np.ndarray) -> any:
    i: any;
    for i in array:
        if i != 0: return i;
    return None;

def rank_column_auto(array: np.array) -> int:
    i: int;
    j: int;
    k: int;
    a: any;
    b: any;
    pivot: any;
    column: int;
    m: np.ndarray;
    arraycopy: np.array = np.array(array, dtype=np.complex64);
    shape: tuple = arraycopy.shape;
    for i in range(shape[0], -1, -1):
        pivot: any = None;
        for j in range(i):
            k: int = shape[0] -i;
            if not isinstance(pivot, np.complex64):
                pivot: any = get_pivot(arraycopy[k]);
                continue; 
            column: int = k + j;
            b: any = get_pivot(arraycopy[column]);
            if not isinstance(b, np.complex64):
                print("has become a problem here!");
                continue;
            a: any = b / pivot * -1;
            arraycopy: np.array = mutate_column_pos(arraycopy, (column, 1), (k, a));
            _print_array_complex(arraycopy, (column, 1), (k, a), pivot);
    i: int = 0;
    for m in arraycopy:
        i: int = i + 1 if sum(m) != 0 else i;
    _print_array_complex(arraycopy);
    return i;

def rank_row_auto (array: np.array) -> int:
    return rank_column_auto(rotate_pos(array));
