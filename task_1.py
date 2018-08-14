#!/usr/bin/env python3

N = 10**6
# Method 1
s1 = sum([i**2 for i in range(int(N**0.5))])
# slower variant
# s1 = sum([i for i in range(10**6) if (i**0.5)%1==0])
print(s1)

# Method 2
s2 = sum(map(lambda x: x*x, range(int(N**0.5))))
print(s2)

# Method 3
s3 = 0
for i in range(int(N**0.5)):
    s3 += i**2
print(s3)