"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string.
"""

def arrayStringsAreEqual(word1, word2):
    s1 = ""
    s2 = ""
    for i in word1:
        s1 += i
    for i in word2:
        s2 += i
    if s1 == s2:
        return True
    else:
        return False


word1 = ["abc", "d", "defg"]
word2 = ["abcddefg"]
res = arrayStringsAreEqual(word1, word2)
print(res)