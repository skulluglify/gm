#! /usr/bin/env python3

import orion;
from orion.vector.concept import *;

a: np.array = np.array([
    [1,2,3,1],
    [2,3,1,4],
    [1,4,2,3],
    [1,3,-3,5]
], dtype=np.int32)

print(a);

print(rank_column_auto(a));

b: np.array = np.array([
[-1,6,2,-3],
[1/3,-2,-2/3,1]
], dtype=np.float32);

print(b);

print(rank_column_auto(b));

c: np.array = np.array([
[2,1,9],
[3,4,0]
], dtype=np.uint32);

print(c);

print(rank_column_auto(c));

## row test

d: np.array = np.array([
[1,2,3,1],
[2,3,1,4],
[1,4,2,3],
[1,3,-3,5],
], dtype=np.int32);

print(d);

print(rank_row_auto(d));