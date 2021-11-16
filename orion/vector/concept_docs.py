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
    ## FATAL: just support only 2d array!
    row: int;
    column: int;
    # shape: tuple = tuple( array.shape[i-1] for i in range(len(array.shape),0,-1) );
    shape: tuple = (array.shape[1], array.shape[0]);
    arrayzeros: np.array = np.zeros([*shape], dtype=array.dtype);
    for row in range(shape[0]):
        for column in range(shape[1]):
            arrayzeros[row][column] = array[column][row];
    return arrayzeros;

def transpose(array: np.array) -> np.array:
    return _zip(array);

def switch_column_pos(array: np.array, a: int, b: int) -> np.array:
    arraycopy: np.array = array.copy();
    arraycopy[a], arraycopy[b] = array[b], array[a];
    return arraycopy;

def switch_row_pos(array: np.array, a: int, b: int) -> np.array:
    return transpose(switch_column_pos(transpose(array), a, b));

def mutate_column_pos(array: np.array, a: tuple, b: tuple) -> np.array:
    arraycopy: np.array = array.copy();
    # after: typing.Iterator = iter([*a, *a]);
    # before: typing.Iterator = iter([*b, *b]);
    # a: np.array = array[next(after)] * next(after);
    A: np.array = array[a[0]] * a[1];
    # b: np.array = array[next(before)] * next(before);
    B: np.array = array[b[0]] * b[1];
    # arraycopy[next(after)] = a + b;
    arraycopy[a[0]] = A + B;
    return arraycopy;

def mutate_row_pos(array: np.array, a: tuple, b: tuple) -> np.array:
    return transpose(mutate_column_pos(transpose(array), a, b));

def revoke_column_pos(array: np.array, a: tuple, b: tuple) -> np.array:
    arraycopy: np.array = array.copy();
    # after: typing.Iterator = iter([*a, *a]);
    # before: typing.Iterator = iter([*b, *b]);
    # m: np.array = array[next(after)];
    m: np.array = array[a[0]];
    # b: np.array = array[next(before)] * next(before);
    B: np.array = array[b[0]] * b[1];
    # m: np.array = (m - b) / next(after);
    m: np.array = (m - B) / a[1];
    # arraycopy[next(after)] = m;
    arraycopy[a[0]] = m;
    return arraycopy;

def revoke_row_pos(array: np.array, a: tuple, b: tuple) -> np.array:
    return transpose(revoke_column_pos(transpose(array), a, b));

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
        z: bool = True;
        for x in m:
            if x != 0:
                z = False;
                break;
        i: int = i + 1 if True else i;
    _print_array_complex(arraycopy);
    return i;

def rank_row_auto (array: np.array) -> int:
    return rank_column_auto(transpose(array));
