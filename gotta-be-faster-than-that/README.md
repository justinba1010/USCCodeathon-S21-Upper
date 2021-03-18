Problem Statement
=================

The primary solution is `solution.py`
The solution can be run with four levels of optimization with `-O0` through `-O3`.
* The first optimization level builds the whole graph and fails after testcase 05
* Optimization levels 1 and 2 are roughly equivalent, solving all test cases except the last
* Optimization level 3 uses a constant amount of memory and could fail but with low probability, solves all testcases

To check solutions, use `profile_solution.py`.
* By default, this runs all testcases and displays the time/memory usage of each.
* With the `--single` flag, it can be uses as a stand in for `solution.py` which reports the profile

To generate testcases, use `gen_samples.py`.
* Each successive test case is roughly 6x as large, using pokemon names for the first two
