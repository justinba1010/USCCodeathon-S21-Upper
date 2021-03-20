# Copyright 2021
# Justin Baum
# Python O(n) solution
# 0.26s for longest test case on Hackerank

n = int(input())
val = list(map(int, input().split()))
names = input().split()
steps = val[0]
print(names[0], end=" ")
max_reach = val[0]
for i in range(1, n - 1):
    new_reach = i + val[i]
    steps -= 1
    if (new_reach > max_reach):
        max_index = i
        max_reach = new_reach
    if (steps == 0):
        print(names[max_index], end=" ")
        steps = max_reach - i
print(names[-1])
