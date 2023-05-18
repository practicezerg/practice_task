"""
You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.
"""
import string
def freqAlphabets(s):
    ideal_string = string.ascii_lowercase
    print(ideal_string)
    slov = {}
    res = ""
    for i, num in zip(ideal_string, range(1,27)):
        slov[str(num)] = i
        if num > 9:
            slov[(str(num)+"#")] = i
    print(slov)
    count_list = []
    for i, count in zip(s,range(len(s))):
        res += i
        if i == "#":
            count_list.append(count)
    print(count_list)
    for i in count_list:
        qq = (s[i-2:i])
        zz =(f"{s[i-2:i]}#")
        res = res.replace(f"{s[i-2:i]}#", slov[f"{s[i-2:i]}#"])
    print(res)
    res_final = ""
    for i in res:
        if i in slov:
            res_final += slov[i]
        else:
            res_final += i
    return res_final







s = "11510#11#12"
res =  freqAlphabets(s)
print(res)