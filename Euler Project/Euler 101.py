

import numpy as np


def generating_function(n):
    return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10

functions = [generating_function(n) for n in range(1,11)]

grand_total = 0
for current_iteration in range(1,11):
    a = np.array([[(y+1)**x for x in range(current_iteration)]for y in range(current_iteration)])
    b = np.array([generating_function(x) for x in range(1,current_iteration+1)])
    x = np.linalg.solve(a, b)
    print(a)
    print(b)
    total = 0
    for power, val in enumerate(x):
        total+=val*(current_iteration+1)**power
    print(f"total: {total}")
    grand_total+=total

print(f'grand total:{grand_total}')