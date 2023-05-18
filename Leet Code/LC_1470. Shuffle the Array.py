"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
"""
def shuffle(nums, n):
    l1 = nums[:n]
    l2 = nums[n:]
    res = []
    for x, y in zip(l1, l2):
        res.append(x)
        res.append(y)
    return res





nums = [1,2,3,4,4,3,2,1]
n = 4
res = shuffle(nums, n)
print(res)