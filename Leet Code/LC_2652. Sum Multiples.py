"""
Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.
Return an integer denoting the sum of all numbers in the given range satisfying the constraint.
"""
def sumOfMultiples(n):
    l = []
    for number in range(1, n+1):
        if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
            l.append(number)
    return sum(l)

n = 9
res = sumOfMultiples(n)
print(res)