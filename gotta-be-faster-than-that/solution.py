#! /usr/bin/env python3

"""
Builds a list of cycles one edge at a time then reports the size of cycles

When adding edge, a dictionary lookup gives a representative vertex for the path containing each end
1. If both endpoints are included in existing paths, combine the two into one path
2. If only one endpoint is in an existing path, add it to that path
3. If neither endpoint is included in an existing path, add the edge as a new path

Since the graph is 2-regular, there are an equal number of edges as vertices
The step for each edge takes O(1) time (assuming an idealized dictionary lookup) so the total time is O(n)
This can be sped up by short circuiting on the first completed cycle - this is still O(n) but probabilistically faster
This technique is sufficiently fast, but uses O(n) memory which is insufficient for large graphs
"""

from collections import deque
from sys import stdin, stderr

DEFAULT_NPAIRS = 100000
DEFAULT_O = 3

def read_input(f=stdin):
  for line in f:
    line = line.strip()
    if not line: continue
    split = line.split()
    assert len(split) == 3
    yield split[0], split[-1]

def path_len(path, O):
  if O >= 2:
    return path[0]
  else:
    return len(path)

def append(path, i, j, O):
  """Connect edge {i,j} to a path which has i as an endpoint"""
  if O >= 2:
    path[0] += 1
    path[1] ^= {i, j}  # Replace i with j
    assert len(path[1]) == 2  # Ensure the set didn't change
  else:
    if path[0] == i:
      path.appendleft(j)
    elif path[-1] == i:
      path.append(j)
    else:
      assert False, "%s is not an endpoint of path %s" % (i, path)

def connect(endpoint_reprs, paths, repr_i, repr_j, i, j, O):
  path_i = paths[repr_i]
  path_j = paths[repr_j]

  if len(path_i) < len(path_j):
    return connect(endpoint_reprs, paths, repr_j, repr_i, j, i, O)  # Make sure we leave the longer list in place

  del endpoint_reprs[i]
  del endpoint_reprs[j]
  del paths[repr_j]

  if O >= 2:
    path_i[0] += path_j[0]
    path_i[1] -= {i}
    path_i[1] |= path_j[1] - {j}
    endpoint_reprs[next(iter(path_j[1] - {j}))] = repr_i
    assert len(path_i[1]) == 2
  else:
    if path_i[0] == i and path_j[0] == j:
      path_i.extendleft(path_j)
      endpoint_reprs[path_j[-1]] = repr_i
    elif path_i[0] == i and path_j[-1] == j:
      path_i.extendleft(reversed(path_j))
      endpoint_reprs[path_j[0]] = repr_i
    elif path_i[-1] == i and path_j[0] == j:
      path_i.extend(path_j)
      endpoint_reprs[path_j[-1]] = repr_i
    elif path_i[-1] == i and path_j[-1] == j:
      path_i.extend(reversed(path_j))
      endpoint_reprs[path_j[0]] = repr_i
    else:
      assert False, "%s and %s are not both endpoints of path %s" % (i, j, path)

def new_path(i, j, O):
  if O >= 2:
    return [2, {i, j}]   # Keep track of length and endpoints rather than the whole path
  else:
    return deque([i,j])  # Keep the whole list as a deque

def run_solution(f=stdin, O=DEFAULT_O, npairs=DEFAULT_NPAIRS):
  """
  Reads file from stdin and outputs the cycle size
  Optimization levels:
    0. Naive: builds full graph then checks that all are the same and outputs the size
    1. Short circuits when a full circuit is completed or a path gets longer than min(k,l)
    2. Does not build build full graphs but rather keeps only endpoints (default)
    3. Keeps a fixed number of paths in memory at a time (success not guaranteed but probable)
  """
  n, k, l = (int(x) for x in next(f).strip().split())
  if k > l: k, l = l, k  # Make sure k <= l

  paths = {}  # representative name -> deque of names
  endpoint_reprs = {}  # name -> representative of group

  for i, j in read_input(f):
    repr_i = endpoint_reprs.get(i, None)
    repr_j = endpoint_reprs.get(j, None)

    if repr_i is not None and repr_j is not None:
      # Connect the two endpoint_reprs and merge paths
      if repr_i == repr_j:
        # Complete cycle
        del endpoint_reprs[i]
        del endpoint_reprs[j]

        if O >= 1:
          return path_len(paths[repr_i], O)
      else:
        connect(endpoint_reprs, paths, repr_i, repr_j, i, j, O)
    elif repr_i is not None:
      # Append {i,j} to the path containing i
      path = paths[repr_i]
      append(path, i, j, O)
      del endpoint_reprs[i]
      endpoint_reprs[j] = repr_i
      if O >= 1 and path_len(path, O) > k:
        return l
    elif repr_j is not None:
      # Append {i,j} to the path containing j
      path = paths[repr_j]
      append(path, j, i, O)
      del endpoint_reprs[j]
      endpoint_reprs[i] = repr_j
      if O >= 1 and path_len(path, O) > k:
        return l
    else:
      # Neither endpoint has been seen yet so make a new path
      if O < 3 or len(paths) < npairs:
        paths[i] = new_path(i, j, O)  # Set i as the new path representative
        endpoint_reprs[i] = endpoint_reprs[j] = i  # Link both endpoint_reprs to representative i

  if O >= 3:
    print("ERROR: no solution found", file=stderr)
    return k  # Guess k
  else:
    cycle_size = len(next(iter(paths.values())))
    assert all(len(path) == cycle_size for path in paths.values())

    return cycle_size

def main(f=stdin, O=DEFAULT_O, npairs=DEFAULT_NPAIRS):
  print(run_solution(f=f, O=O, npairs=npairs))

if __name__ == "__main__":
  import argparse
  argp = argparse.ArgumentParser("Determines size of cycles within a graph of either all k-cycles or all l-cycles")
  argp.add_argument("-O", default=DEFAULT_O, type=int, help="Optimization level (default: 2)")
  argp.add_argument("--pairs", default=DEFAULT_NPAIRS, type=int, help="Number of pairs to keep for -O3")
  argv = argp.parse_args()
  main(O=argv.O, npairs=argv.pairs)
