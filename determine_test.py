#! /usr/bin/env python3 

import orion;
from orion.vector.determine import *;

a: np.array = np.array([
    1, 2, 3
], dtype=np.uint32);

print(det.permute(a));

b: np.array = np.array([
    6, 4, 5, 3, 1, 2
], dtype=np.uint32);


# 6 > 4 5 3 1 2 > 5
# 4 > 5 3 1 2 > 3
# 5 > 3 1 2 > 3
# 3 >  1 2 > 2
# 1 > 2 > 0
print(det.inverse(b));
