#!/usr/bin/env python3
from functools import reduce
from timeit import default_timer


""" Recursive solution """
def make_cache(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if args in cache.keys():
            return cache[args]
        else:
            cache[args] = func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper
@make_cache
def collatz_steps_recoursive(n, acc=0):
    if n < 1 or n % 1 != 0:
        raise ValueError(str(n) + " is not natural a number")
    if n == 1:
        return acc
    else:
        n = n/2 if n % 2 == 0 else 3*n + 1
        return collatz_steps_recoursive(n, acc + 1)


# Test 1
assert collatz_steps_recoursive(16) == 4
assert collatz_steps_recoursive(12) == 9
assert collatz_steps_recoursive(1000000) == 152

N = 1000000
st = default_timer()
rec_result = collatz_steps_recoursive(N)
print("Recursive collatz_steps:\nN = {}\nProcessing took: {} s\nResult: {} steps\n"
    .format(N, default_timer() - st, rec_result))

N = 12331313116718841718481471486146814871414183187817489171849714
try:
    rec_result = collatz_steps_recoursive(N)
except:
    print("Recursive collatz_steps:\nFailed to process N = {}\nMaximum recursion depth exceeded\n".format(N))



""" Generator-based solution """
def collatz_steps(n):
    # Validate input
    if n < 1 or not isinstance(n, int) != 0:
        raise ValueError(str(n) + " is not natural a number")
    # Initial value of collatz sequence
    collatz_nums = [n]
    # Fill collatz nums with actual values untill last number is equal 1
    step_lst = [collatz_nums.append(i/2) if i % 2 == 0 else collatz_nums.append(3 * i + 1) 
                for i in collatz_nums if collatz_nums[-1] != 1]
    # step_lst is list of Nones with len equal to number of steps
    return len(step_lst)


# Test 2
N = 1000000
st = default_timer()
result = collatz_steps(N)
print("Generator-based collatz_steps:\nN = {}\nProcessing: took {} s\nResult: {} steps\n"
    .format(N, default_timer() - st, result))

N = 12331313116718841718481471486146814871414183187817489171849714
st = default_timer()
result = collatz_steps(N)
print("Generator-based collatz_steps:\nN = {}\nProcessing: took {} s\nResult: {} steps\n"
    .format(N, default_timer() - st, result))

""" One-line solution """
collatz_steps = lambda N: (lambda N, lst=[N]: reduce(lambda x,y: x+1, [lst.append(i/2) if i%2==0 else lst.append(3*i+1) for i in lst if lst[-1]!=1], 0))(N) if isinstance(N,int) and N > 0 else exec('raise ValueError("{}({}) is not natural number")'.format(type(N).__name__, N)) 


# Test 3
assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152

N = 1000000
st = default_timer()
result = collatz_steps(N)
print("One-line collatz_steps:\nN = {}\nProcessing: took {} s\nResult: {} steps\n"
    .format(N, default_timer() - st, result))

N = 12331313116718841718481471486146814871414183187817489171849714
st = default_timer()
result = collatz_steps(N)
print("One-line collatz_steps:\nN = {}\nProcessing: took {} s\nResult: {} steps\n"
    .format(N, default_timer() - st, result))