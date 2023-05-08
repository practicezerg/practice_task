"""Given a string s, reverse the order of characters in each word within a sentence while still preserving
whitespace and initial word order."""
def reverseWords(s):
    l = s.split()
    res = []
    for i in l:
        res.append(i[::-1])
    return " ".join(res)




s = "Let's take LeetCode contest"
res = reverseWords(s)
print(res)