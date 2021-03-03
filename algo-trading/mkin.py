#!/usr/bin/python3
import random
(k, n) = [int(x) for x in input().split()]

arr = [random.randint(1, k) for _ in range(n)]

namefile = open("names.txt", "r")
names = [name.strip() for name in namefile]
names = random.sample(names, k=n)


print(n)
print(" ".join(map(str, arr)))
print(" ".join(names))

