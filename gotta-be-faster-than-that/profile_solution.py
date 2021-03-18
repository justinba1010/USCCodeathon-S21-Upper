#! /usr/bin/env python3

import resource
from time import time
from sys import stdin
import os

from solution import run_solution, DEFAULT_O, DEFAULT_NPAIRS

TIME_LIMIT=10
MEM_LIMIT=512

def main_limited(f=stdin, time_limit=TIME_LIMIT, mem_limit=MEM_LIMIT, O=DEFAULT_O, npairs=DEFAULT_NPAIRS):
  start = time()
  output = run_solution(f=f, O=O, npairs=npairs)
  execution_time = time() - start
  max_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.

  time_success = execution_time <= time_limit
  mem_success = max_mem <= mem_limit

  print("--- Overview ---")
  print("Output:        ", output)
  print("Execution time:", "% 10g" % execution_time, "s", "" if time_success else "(TIMEOUT)")
  print("Memory usage:  ", "% 10g" % max_mem, "mb", "" if mem_success else "(OUT OF MEMORY)")
  print("----------------")

  return time_success and mem_success, output

def check_all(time_limit=TIME_LIMIT, mem_limit=MEM_LIMIT, O=DEFAULT_O, npairs=DEFAULT_NPAIRS):
  testcases = sorted(os.listdir("testcases/input/"))
  for testcase in testcases:
    ifile = os.path.join("testcases/input/", testcase)
    ofile = os.path.join("testcases/output/", "output" + testcase.lstrip("input"))

    print("TESTCASE", testcase)
    with open(ifile) as i, open(ofile) as o:
      correct_output = int(next(o).strip())
      success, output = main_limited(f=i, time_limit=time_limit, mem_limit=mem_limit, O=O, npairs=npairs)
      if output != correct_output:
        print("WRONG ANSWER: Correct %d, Given %d" % (correct_output, output))
        success = False
    print()
    if not success:
      return False
  return True

if __name__ == "__main__":
  import argparse
  argp = argparse.ArgumentParser("Tests time and memory usage of solution")
  argp.add_argument("-O", default=DEFAULT_O, type=int, help="Optimization level (default: 2)")
  argp.add_argument("--time-limit", default=TIME_LIMIT, type=float, help="Time limit (s)")
  argp.add_argument("--mem-limit", default=MEM_LIMIT, type=float, help="Memory limit (mb)")
  argp.add_argument("--pairs", default=DEFAULT_NPAIRS, type=int, help="Number of pairs to keep for -O3")
  argp.add_argument("--single", action="store_true", help="Profiles a single testcase, reading from stdin")
  argv = argp.parse_args()

  if argv.single:
    success = main_limited(time_limit=argv.time_limit, mem_limit=argv.mem_limit, O=argv.O, npairs=argv.pairs)
  else:
    success = check_all(time_limit=argv.time_limit, mem_limit=argv.mem_limit, O=argv.O, npairs=argv.pairs)

  print("CHECK", "PASSED" if success else "FAILED")

  exit(int(not success))
