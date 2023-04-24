"""Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
 For example:"""
import re

def mine(url):
    print(url)
    url = url.lstrip("https://www.")

    print(url)




def domain_name(url):
    if url.startswith("https://www.") == True:
        url = url.replace("https://www.","")
        num_pos_1st_dot = url.index('.')
        return url[:num_pos_1st_dot]
    elif url.startswith("http://www.") == True:
        url = url.replace("http://www.", "")
        num_pos_1st_dot = url.index('.')
        return url[:num_pos_1st_dot]
    else:
        url = url.replace("www.", "")
        num_pos_1st_dot = url.index('.')
        return url[:num_pos_1st_dot]


url = "http://google.co.jp"
# url = "http://google.com"
# url = "http://github.com/carbonfive/raygun"
# url = "http://www.zombie-bites.com"
res = domain_name(url)
# res = mine(url)
print(res)