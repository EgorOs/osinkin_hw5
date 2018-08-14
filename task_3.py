#!/usr/bin/env python3
from functools import reduce

collatz_steps = lambda N: (lambda N, lst=[N]: reduce(lambda x,y: x+1, [lst.append(i/2) if i%2==0 else lst.append(3*i+1) for i in lst if lst[-1]!=1], 0))(N) if isinstance(N,int) and N > 0 else exec('raise ValueError("{}({}) is not natural number")'.format(type(N).__name__, N)) 

assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152

# print(collatz_steps(12331313116718841718481471486146814871414183187817489171849714)) # Recursive function failes here
