#! /usr/bin/env python3

import typing;
import numpy as np;
from vector.determine \
import sarrus_column_auto;
from vector.concept \
import transpose;

def cofactor_minor (array: np.array):

    ## debug
    array: np.array = np.array([*map(lambda x: [*map(lambda c: c.real, x)],array)], dtype=np.int64);

    print(array);

    shape: typing.Tuple = array.shape;
    rows: int = shape[0];
    columns: int = shape[1];

    child_shape: typing.Tuple = tuple(map(lambda x: x-1, shape));
    child_nodes: typing.List = [];

    for xrow in range(rows):
        for xcolumn in range(columns):

            yrow: int = 0;
            ycolumn: int = 0;
            child: np.array = np.zeros(child_shape, dtype=array.dtype);

            mp: bool = not ((xrow%2)^(xcolumn%2));

            for row in range(rows):
                if row == xrow: continue;
                for column in range(columns):
                    if column == xcolumn: continue;
                    child[yrow][ycolumn] = array[row][column];
                    ycolumn += 1;
                ycolumn = 0;
                yrow += 1;
            
            child_nodes.append((
                mp, (xrow, xcolumn), child
            ));
    
    temp: np.array = np.zeros(shape, dtype=array.dtype);
    
    for node in child_nodes:

        mp, pos, child = node;
        row, column = pos;

        print("pos", *pos);

        value: child.dtype = sarrus_column_auto(child);
        print("+1" if mp else "-1", end=" * ");
        print(value, end=" = ");

        if not mp: value *= -1;
        temp[row][column] = value;

        print(value)

        print()
    
    print(temp);

    return temp;

def adjoint_matrix (array: np.array):

    return transpose(cofactor_minor(array));