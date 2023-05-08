"""
You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.
There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.
For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).
Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.
"""

import string
def replaceDigits(s):
    string_ideal = string.ascii_lowercase
    res, index_symbol = "", 0
    for i in s:
        if i in string_ideal:
            index_symbol = string_ideal.index(i)
            res += i
        else:
            res += string_ideal[int(i) + index_symbol]
    return res






s = "a1b2c3d4e"
res =  replaceDigits(s)
print(res)