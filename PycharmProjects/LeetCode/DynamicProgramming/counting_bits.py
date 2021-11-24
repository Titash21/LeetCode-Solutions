"""
Given an integer n, return an array ans of length n + 1
such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
"""
def countBits(n: int):
    dictionary = {}
    dictionary[0] = 0
    dictionary[1] = 1
    result = [0]
    for i in range(1, n + 1):
        count = i % 2 + dictionary[i // 2]
        dictionary[i] = count
        result.append(count)
    return result

countBits(3)