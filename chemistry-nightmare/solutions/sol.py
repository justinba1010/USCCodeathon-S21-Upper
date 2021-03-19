kimport sys
from collections import defaultdict


def dfs_helper(a,b, visited):
   if a == b:
      return True
   visted.add(a)
   if len(visted) == num_nodes:
      return False
   for neighbor in adj[a]:
      if neighbor not in visited:
         dfs_helper(neighbor,b,visited)

def dfs(a,b):
   visited = set()
   dfs_helper(a,b,visited)

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
   char_pairs = zip(w1,w2)
   if not len(w1) == len(w2):
	print('no')
   else:
      for a,b in char_pairs:
         if not dfs(a,b):
            print('no')
            break
         else:
            print('yes')



