"""If you can't sleep, just count sheep!!
Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...".
Input will always be valid, i.e. no negative integers."""
def count_sheep(n):
    x = 1
    res = ""
    while x <= n:
        string = f"{x} sheep..."
        res = res + string
        x+=1
    return res


n = 3
res = count_sheep(n)
print(res)
