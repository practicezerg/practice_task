"""
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent
if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.
"""
def countConsistentStrings(allowed, words):
    count, num = 0, 0
    for word in words:
        for char in word:
            if char in allowed:
                 num += 1
            else:
                num = 0
        if len(word) == num:
            count += 1
        num = 0
    return count


allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
res = countConsistentStrings(allowed, words)
print(res)