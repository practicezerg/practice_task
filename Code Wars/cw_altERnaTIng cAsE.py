"""
Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase
/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter
 becomes uppercase and each uppercase letter becomes lowercase. For example:
"""


def to_alternating_case(string):
    return string.swapcase()



string = "HELLO WORLD"
res = to_alternating_case(string)
print(res)