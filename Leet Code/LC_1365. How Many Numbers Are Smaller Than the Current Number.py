"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each
nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
"""

def smallerNumbersThanCurrent(nums):
    res = []
    for num in nums:
        count = 0
        for num2 in nums:
            if num2 < num:
                count += 1
        res.append(count)
    return res


nums = [6,5,4,8]
res = smallerNumbersThanCurrent(nums)
print(res)