#!/usr/bin/python3
import random
(k, n) = [int(x) for x in input().split()]

arr = [random.randint(1, k) for _ in range(n)]

namefile = open("names.txt", "r")
names = [name.strip() for name in namefile]
if (n < 18000):
    names = random.sample(names, k=n)
else:
    newnames = names[:]
    for i in range(n//15000):
        newnames += [name + str(i) for name in names]
    names = random.sample(newnames, k=n)

print(n)
print(" ".join(map(str, arr)))
print(" ".join(names))

