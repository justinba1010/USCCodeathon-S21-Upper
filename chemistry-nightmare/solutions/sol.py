import sys
from collections import defaultdict


def dfs_helper(a,b, visited):
   if a == b:
      return True
   visited.add(a)
   flags = []
   for neighbor in adj[a]:
      if neighbor not in visited:
        flags.append(dfs_helper(neighbor,b,visited))
        # print(dfs_helper(neighbor,b,visited))
   return any(flag for flag in flags)

def dfs(a,b):
   visited = set()
   return dfs_helper(a,b,visited)

# Driver Code
m,n = sys.stdin.readline().split(' ')
n = n.strip()
adj = defaultdict(list)

for i in range(int(m)):  # construct adjacency list from translations
   a,b = sys.stdin.readline().split(' ')
   b = b.strip()
   adj[a].append(b)

num_nodes = len(adj)

for i in range (int(n)):
   w1, w2 = sys.stdin.readline().split(' ')
   w2 = w2.strip()
   char_pairs = zip(w1,w2)
   if not len(w1) == len(w2):
      print('no')
   else:
      for a,b in char_pairs:
         # print(a,b)
         if not dfs(a,b):
            print('no')
            break
      else:
         print('yes')
