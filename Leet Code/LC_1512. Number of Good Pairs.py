"""
Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.
Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
"""
def numIdenticalPairs(nums):
    res = 0
    for i, n in zip(nums, range(len(nums))):
        count_pos = nums[n+1:].count(i)
        res += count_pos
    return res


nums = [1,2,3,1,1,3]
res = numIdenticalPairs(nums)
print(res)

