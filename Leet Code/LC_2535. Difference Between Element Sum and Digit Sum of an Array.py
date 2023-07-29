"""
You are given a positive integer array nums.
The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.
Note that the absolute difference between two integers x and y is defined as |x - y|.
"""
def differenceOfSum(nums):
    sum_nums  = sum(nums)
    sum_str_nums = 0
    for num in nums:
        if num > 9:
            for i in str(num):
                sum_str_nums += int(i)
        else:
            sum_str_nums += num
    print(sum_nums)
    print(sum_str_nums)
    return abs(sum_nums-sum_str_nums)






nums = [1,15,6,3]
res = differenceOfSum(nums)
print(res)