#! /usr/bin/env python3

import orion;
from orion.vector.concept_docs \
import *;
from orion.vector.determine \
import *;
from orion.vector.minor \
import *;
from orion.vector.invers \
import *;

d: np.array = np.array([
[ 1, -1, 1, -1 ],
[ 1, -1, 3, 2 ],
[ 4, 2, 1, 3 ],
[ 3, 1, 1, -4 ]
], dtype=np.int64);

print("===");
print(cofactor_column_auto(d));
