#!/usr/bin/env python3
from functools import reduce
from time import time


# Problem 9
N = 1000
start_time = time()
solution_9 = \
    [a * b * (N - a - b) for a in range(1, N // 3) for b in range(a, N // 2) if
     a ** 2 + b ** 2 == (N - a - b) ** 2 and a + b + (N - a - b) == N][0]
print('Problem 9 result: {}\nProcessing took: {}\n'
      .format(solution_9, time() - start_time))

# Problem 6
N = 100
start_time = time()
solution_6 = sum([n for n in range(N + 1)]) ** 2 - sum(
    [n * n for n in range(N + 1)])
print('Problem 6 result: {}\nProcessing took: {}\n'
      .format(solution_6, time() - start_time))

# Problem 48
N = 1000
start_time = time()
solution_48 = str(sum([i ** i for i in range(N + 1)]))[-10:]
print('Problem 48 result: {}\nProcessing took: {}\n'
      .format(solution_48, time() - start_time))

# Problem 40
N = 1000000
start_time = time()
irr_dec_frac = ''.join([str(n) for n in range(N)])
solution_40 = reduce(lambda x, y: int(x) * int(y),
                     [irr_dec_frac[i] for i in
                      [10 ** r for r in range(len(str(N)))]])
print('Problem 40 result: {}\nProcessing took: {}\n'
      .format(solution_40, time() - start_time))
