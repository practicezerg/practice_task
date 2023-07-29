"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""
def runningSum(nums):
    res = []
    res.append(nums[0])
    for i in nums[1:]:
        res.append(i+res[-1])
    return res


nums = [1,2,3,4]
res = runningSum(nums)
print(res)