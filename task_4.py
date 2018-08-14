#!/usr/bin/env python3
from functools import reduce

# Problem 9
N = 1000
solution_9 = \
    [a * b * (N - a - b) for a in range(1, N // 3) for b in range(a, N // 2) if
     a ** 2 + b ** 2 == (N - a - b) ** 2 and a + b + (N - a - b) == N][0]
print('Problem 9 result: ', solution_9)

# Problem 6
N = 100
solution_6 = sum([n for n in range(N + 1)]) ** 2 - sum(
    [n * n for n in range(N + 1)])
print('Problem 6 result: ', solution_6)

# Problem 48
N = 1000
solution_48 = str(sum([i ** i for i in range(N + 1)]))[-10:]
print('Problem 48 result: ', solution_48)

# Problem 40
N = 1000000
solution_40 = reduce(lambda x, y: x * y,
                     [[int(d) for d in
                       ''.join([str(n) for n in range(0, N + 1)])][i]
                      if i in {10 ** r for r in range(len(str(N)))} else 1
                      for i in range(N + 1)])
print('Problem 40 result: ', solution_40)
