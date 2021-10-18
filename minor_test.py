#! /usr/bin/env python3

import orion;
from orion.vector.concept_docs import *;
from orion.vector.minor import *;

a: np.array = np.array([
[3,  2, -1],
[1,  6,  3],
[2, -4,  0]
], dtype=np.complex64)

a = adjoint_matrix(a);

print();
print(a);