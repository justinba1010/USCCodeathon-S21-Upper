#def groupings(n):
#    if n == 1:
#        yield 'a'
#        return
#    for i in range(1,n):
#        for x in groupings(i):
#            for y in groupings(n - i):
#                yield '(' + x + y + ')'

from functools import lru_cache

#@lru_cache(maxsize=None)
#def fib_shifted(n):
#    if n == 1:
#        return 2
#    if n == 2:
#        return 3
#    return fib_shifted(n-1) + fib_shifted(n-2)


def building_colors(n):
    if n == 1:
        yield '0'
        yield '1'
        return
    if n == 2:
        yield '00'
        yield '01'
        yield '10'
        return
    for x in building_colors(n-1):
        yield '0' + x
    for y in building_colors(n-2):
        yield '10' + y

#@lru_cache(maxsize=None)
def build_colors(n):
   if n == 1:
      return ['0','1']
   if n == 2:
      return ['00','01','10']
   L = []
   for x in build_colors(n-1):
      L.append('0' + x)
   for y in build_colors(n-2):
      L.append('10' + y)
   return L

## buildings driver code
n = int(input())
ans = build_colors(n)
for a in ans:
   print(a)
#print(fib_shifted(n))
#assert len(ans) == fib_shifted(n)
assert sorted(ans) == ans

## groupings driver code
#n = int(input('Max # of terms:'))
#for i in range(1,n+1):  
#    print([x for x in groupings(i)])


