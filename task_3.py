#!/usr/bin/env python3
from functools import reduce

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
def collatz_steps(n, acc=0):
    if n < 1 or n % 1 != 0:
        raise ValueError(str(n) + " is not natural a number")
    if n == 1:
        return acc
    else:
        n = n/2 if n % 2 == 0 else 3*n + 1
        return collatz_steps(n, acc + 1)


assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152

# print(collatz_steps(10**7))

# N = 12
# lst = [N]
# for i in range(N):
#     if lst and lst[-1]!=1:
#         n = lst[-1]
#         n = n/2 if n%2==0 else n*3+1
#         lst.append(n)

# print(lst)

# print(reduce(lambda x,y: x+1, lst, -1))

# lol = []
# [lol.append(i) if ('lol' in globals()) else globals().update({'lol':[i]}) for i in range(N)]
# print(lol)

# lst = [i/2 if i%2==0 else 3*i+1 for i in range(N*4) if i<=N]
# print(lst)

# lst = [1,2,3]
# nl = [lst.append(i) for i in lst if len(lst)<1000]
# print(len(nl))


# print([globals().update({'Li':[]}) for i in ('a' or globals()['Li']) if len('Li')<1000])
# print(Li)
# print(len(nl))

# lst = [12331313116718841718481471486146814871414183187817489171849714]
# lst = [12]
# print(reduce(lambda x,y: x+1, [lst.append(i/2) if i%2==0 else lst.append(3*i+1) for i in lst if lst[-1]!=1], 0))

def F(N):
    lst = [N]
    # print(locals())
    return reduce(lambda x,y: x+1, [lst.append(i/2) if i%2==0 else lst.append(3*i+1) for i in lst if lst[-1]!=1], 0)
    # return reduce(lambda x,y: x+1, [locals().update({'N':[*[locals()['N']]]+[i/2] if isinstance(locals()['N'], int) else [*locals()['N']]+[i/2]}) if i%2==0 else locals().update({'N':[*[locals()['N']]]+[i*3+1] if isinstance(locals()['N'], int) else [*locals()['N']]+[i*3+1]}) for i in [N] if locals()['N'][-1]!=1], 0) 
print(F(12331313116718841718481471486146814871414183187817489171849714))