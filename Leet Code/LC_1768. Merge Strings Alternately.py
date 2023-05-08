"""You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with
word1. If a string is longer than the other, append the additional letters onto the end of the merged string."""
def mergeAlternately(word1, word2):
    res = ""
    for a, b in zip(word1, word2):
        res += a + b
    if len(word1) > len(word2):
        res += word1[len(word2):]
    elif len(word1) < len(word2):
        res += word2[len(word1):]
    else:
        return res
    return res


word1 = "cdf"
word2 = "a"
res = mergeAlternately(word1, word2)
print(res)