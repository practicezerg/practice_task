"""
Given an integer num, return the number of digits in num that divide num.
An integer val divides nums if nums % val == 0.
"""
def countDigits(num):
    count = 0
    for i in str(num):
        if num % int(i) == 0:
            count += 1
    return count



num = 121
res = countDigits(num)
print(res)