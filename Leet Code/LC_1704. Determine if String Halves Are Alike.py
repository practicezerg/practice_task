"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first
half and b be the second half.
Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
Notice that s contains uppercase and lowercase letters.
Return true if a and b are alike. Otherwise, return false.
"""
def halvesAreAlike(s):
    list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    left, right = 0, 0
    for i, x in zip(s[0:(int(len(s)/2))], s[int(len(s)/2):]):
        if i in list:
            left += 1
        if x in list:
            right += 1
    if left == right:
        return True
    return False




s = "textbook"
res =  halvesAreAlike(s)
print(res)