#! /usr/bin/env python3

import typing;
import numpy as np;

## r column
## o column
## w column

## H > column

## K > row

## zip row > column
## zip column > row

def _print_array_complex(array: np.array, *args, **kwargs):
    arraycopy: np.array = np.zeros(array.shape, dtype=np.float128);
    for row in range(array.shape[0]):
        for column in range(array.shape[1]):
            m: any = array[row][column];
            if isinstance(m, complex):
                arraycopy[row][column] = round(m, 2);
            else:
                arraycopy[row][column] = round(m, 2);
    print(arraycopy, *args, **kwargs);

def _zip(array: np.array) -> np.array:
    shape: tuple = tuple( array.shape[i-1] for i in range(len(array.shape),0,-1) );
    arrayzeros: np.array = np.zeros([*shape], dtype=array.dtype);
    for row in range(shape[0]):
        for column in range(shape[1]):
            arrayzeros[row][column] = array[column][row];
    return arrayzeros;

def change_pos(array: np.array) -> np.array:
    # return np.array([*zip(*array)], dtype=array.dtype); # could't handle huge size!
    return _zip(array);

def switch_pos(array: np.array, a: int, b: int) -> np.array:
    arraycopy: np.array = array.copy();
    arraycopy[a], arraycopy[b] = array[b], array[a];
    return arraycopy;

def mutate_pos(array: np.array, a: tuple, b: tuple) -> np.array:

    _print_array_complex(array, a, b);

    arraycopy: np.array = array.copy();
    after: typing.Iterator = iter([*a, *a]);
    before: typing.Iterator = iter([*b, *b]);
    a: np.array = array[next(after)] * next(after);
    b: np.array = array[next(before)] * next(before);
    arraycopy[next(after)] = a + b;
    return arraycopy;

def revoke_pos(array: np.array, a: tuple, b: tuple) -> np.array:

    _print_array_complex(array, a, b);

    arraycopy: np.array = array.copy();
    after: typing.Iterator = iter([*a, *a]);
    before: typing.Iterator = iter([*b, *b]);
    m: np.array = array[next(after)];
    b: np.array = array[next(before)] * next(before);
    m: np.array = (m - b) / next(after);
    arraycopy[next(after)] = m;
    return arraycopy;

def search_pivot(array: np.ndarray) -> any:
    
    for i in array:
    
        if i != 0: return i;
    
    return None;

def rank_column_auto(array: np.array) -> int:

    arraycopy: np.array = np.array(array, dtype=np.complex128);
    # arraycopy.dtype = np.example128; ## handle float Significand (also mantissa or coefficient)
    
    shape: tuple = array.shape;

    for i in range(shape[0], -1, -1):
        
        pivot: any = None;
        
        for j in range(i):
            
            k: int = shape[0] -i;
            
            if not pivot:
                pivot: any = search_pivot(arraycopy[k]);
                continue;
            
            column: int = k + j;
            b: any = search_pivot(arraycopy[column]);

            if not b:
                print("has become a problem here!");
                break;
            
            a: any = b / pivot * -1;
            arraycopy: np.array = mutate_pos(arraycopy, (column, 1), (k, a));
            print(pivot.real, end="\n\n");

    i: int = 0;
    for c in arraycopy:
        i: int = i + 1 if sum(c) != 0 else i;

    _print_array_complex(arraycopy);

    return i;

def rank_row_auto (array: np.array) -> int:
    return rank_column_auto(change_pos(array));
