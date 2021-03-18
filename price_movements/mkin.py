#!/usr/bin/python3
import random
(k, n) = [int(x) for x in input().split()]
arr = [random.randint(-2**20, 2**20) for _ in range(n)]

print(n)
print(" ".join(map(str, arr)))
