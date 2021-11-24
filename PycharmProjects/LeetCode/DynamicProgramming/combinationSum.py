def combo(arr, target):

    if target == 0: return []
    if target < 0: return None
    allCombinations = []
    for i in range(len(arr)):
        diff = target - arr[i]
        result = combo(arr, diff)
        if result is not None:
            finals = [item for item in result]
            finals.append(arr[i])
            allCombinations.append(finals)
            print("target",target, "arr[i]", arr[i], "result=", result,"finals=", finals)
            # return finals
    return allCombinations

print(combo([2,3,6,7],7))