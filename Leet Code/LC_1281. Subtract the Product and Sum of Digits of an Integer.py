# -*- encoding: utf-8 -*-
"""Given an integer number n, return the difference between the product of its digits and the sum of its digits."""


def subtractProductAndSum(n):
    mult = 1
    suma = 0
    for num in str(n):
        suma += int(num)
        mult *= int(num)
    return mult - suma

n = 4421
res = subtractProductAndSum(n)
print(res)

