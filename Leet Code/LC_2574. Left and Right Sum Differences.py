"""Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:
answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:
leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element,
leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element,
rightSum[i] = 0.
Return the array answer."""


def leftRightDifference(nums):
    res = []
    for num, pos in zip(nums, range(len(nums))):
        res.append(abs(sum(nums[:pos]) - sum(nums[pos + 1:])))
    return res


nums = [10,4,8,3]
res = leftRightDifference(nums)
print(res)



