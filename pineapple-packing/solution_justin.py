# Copyright 2021
# Justin Baum
# Pineapple Packing

def sol(n):
    x = (n + 1) // 3
    if x == 0:
        return ""
    y = (n - x*3)
    if (y == -1):
        return sol(x) + "L"
    if (y == 0):
        return sol(x) + "M"
    if (y == 1):
        return sol(x) + "R"

n = int(input())
print(sol(n))
