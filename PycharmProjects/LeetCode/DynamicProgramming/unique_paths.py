"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

"""

import numpy as np
def uniquePaths(m: int, n: int) -> int:

    def dp(m, n, memodict={}):
        # are the paths in the memo object ?
        key = str(m) + ',' + str(n)
        if key in memodict:
            return memodict[key]
        if m == 1 and n == 1:
            return 1
        elif m == 0 or n == 0:
            return 0
        memodict[key] = dp(m - 1, n, memodict) + dp(m, n - 1, memodict)
        return memodict[key]

    return dp(m, n, {})

print(uniquePaths(3,7))

print()