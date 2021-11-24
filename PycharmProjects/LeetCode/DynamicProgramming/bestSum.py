"""
Given a target and a array of numbers if it is possible to generate the targetsum using the elements of the array,
return the best combinations which sum to the target
if there is a tie you can return any of the combination

You can use the elements of the array any number of times to create the target sum
Eg  howSum(7, [5,4,3,7]) ----> return [7]
howSum(8, [2,3,4,5] ) --> [4,4] [2,2,2] [2,4,2]
"""

def bestSum(target, arr, memo={}):
    if target == 0: return []
    if target < 0: return None
    shortestComb = None #initialized to none so assume that there will not be any possible combinations
    # this tries all the branches
    for item in arr:
        diff = target - item
        result = bestSum(diff, arr)
        if result!=None:
            comb = [iem for iem in result]
            comb.append(item)
            if shortestComb == None or len(shortestComb) > len(comb):
                shortestComb = comb
    return shortestComb

def bestSumMemo(target, arr, memo={}):
    if target in memo:
        return memo[target]
    if target == 0: return []
    if target <0 : return None
    shorttestCombo = None
    for item in arr:
        diff = target - item
        # print("target=", target, "item=", item, "diff", diff, "memo", memo)
        result = bestSum(diff, arr, memo)
        if result is not None:
            new_result = [i for i in result]
            new_result.append(item)
            # print(new_result)
            if shorttestCombo==None or len(new_result) < len(shorttestCombo):
                memo[target] = new_result
                shorttestCombo = new_result
    return shorttestCombo

print("Result Memo", bestSumMemo(7, [4,7,3,5]))
print("Result ", bestSum(7, [4,7,3,5]))

print("Result Memo", bestSumMemo(8, [2,3,5]))
print("Result ", bestSum(8, [2,3,5]))

print("Result Memo", bestSumMemo(100, [2,3,5]))
print("Result ", bestSum(8, [1,4,5]))

print("Result Memo", bestSumMemo(100, [2,3,5]))
print("Result ", bestSum(100, [2,3,5]))



