"""
Given a target and a array of numbers, return boolean True / False
if it is possible to generate the targetsum using the elements of the array
You can use the elements of the array any number of times to create the target sum
Eg  [2,4] ----> 28 then (14*2)
"""
def canSum(target, array):

    if target == 0: return True
    if target < 0: return False
    for i in range(len(array)):
        diff = target - array[i]
        if canSum(diff, array) == True:
            return True
    return False


def canSumDynamicProgramming(target, array, memo = {}):
    #cache
    if target in memo:return memo[target]
    if target == 0: return True
    if target < 0: return False
    for i in range(len(array)):
        diff = target - array[i]
        if canSumDynamicProgramming(diff, array, memo):
            memo[target] = True
            return True
    memo[target] = False
    return False

print("result", canSumDynamicProgramming(target=7, array=[5,3,4,7], memo={}))
print("result", canSum(target=7, array=[5,3,4,7]))

# print("result", canSumDynamicProgramming(target=8, array=[5,3,4,7], memo={}))
print("result", canSumDynamicProgramming(target=7, array=[2,4], memo={}))
print("result", canSum(target=7, array=[2,4]))
print("result", canSumDynamicProgramming(target=300, array=[7,14]))