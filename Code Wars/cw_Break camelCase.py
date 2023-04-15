"""Complete the solution so that the function will break up camel casing, using a space between words"""
def solution(s):
    res = ""
    for i in s:
        if i.isupper() == True:
            res = res + " " + i
        else:
            res = res + i
    return res


s = "breakCamelCase"
res = solution(s)
print(res)