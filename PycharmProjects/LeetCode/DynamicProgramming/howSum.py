import time
"""
Given a target and a array of numbers if it is possible to generate the targetsum using the elements of the array,
return the elements of the array that create the sum
If there are many combinations, then return only one
You can use the elements of the array any number of times to create the target sum
Eg  howSum(7, [5,4,3,7]) ----> [7] [4,3] [3,4]
howSum(8, [2,3,4,5] ) --> [4,4] [2,2,2] [2,4,2]
"""

def howSum(target, arr):

    if target == 0: return []
    if target <0: return None
    for i in range(len(arr)):
        diff = target - arr[i]
        result = howSum(diff, arr)
        if result is not None:
            finals = [item for item in result]
            finals.append(arr[i])
            # print("target",target, "arr[i]", arr[i], "result=", result,"finals=", finals)
            return finals
    return None

def howSumMemoize(target, arr, memo={}):
    #caching
    if target in memo:
        return memo[target]
    if target == 0: return []
    if target < 0 : return None
    for item in arr:
        diff = target - item
        result = howSumMemoize(diff, arr, memo)
        if result is not None:
            final_arr = [itm for itm in result]
            final_arr.append(item)
            memo[target] = final_arr # we equate it to the target because ideally this is the solution of the target input
            return memo[target]
    memo[target] = None
    return memo[target]

print("ans =",howSum(7, [5,4,3,7]))
print("Memoize ans =",howSumMemoize(7, [5,4,3,7]))
print("ans =",howSum(8, [2,4]))
print("Memoize howSumMemoize =",howSum(8, [2,4]))
start_time = time.time()
print("ans =",howSum(300, [7,14]))
end_time = time.time()
print("Recursion time", end_time-start_time)

start_time = time.time()
print("Memoize howSumMemoize =",howSum(300, [7,14]))
end_time = time.time()
print("memoize time:",end_time-start_time)