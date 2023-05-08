"""
You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words,
the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.
Return the number of '*' in s, excluding the '*' between each pair of '|'.
Note that each '|' will belong to exactly one pair.
"""
def countAsterisks(s):
    round, res = 0, ""
    for symbol in s:
        if symbol == "|":
            round += 1
        else:
            if round % 2 == 0:
                res += symbol
    return res.count("*")




s = "l|*e*et|c**o|*de|"
res = countAsterisks(s)
print(res)