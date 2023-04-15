"""Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
 For example:"""
def domain_name(url):
    num = url.count(".")
    num_pos_1st_dot = url.index('.')
    res = ""
    if num > 1:
        num_dot = 0
        for i in url:
            if i == ".":
                num_dot += 1
                if num_dot == 2:
                    print("Две точки! Руби")
                    print(url[num_pos_1st_dot+1:])
                    return res[num_pos_1st_dot+1:]
            res = res + i
    else:
        print("точка одна")
        print(url[:num_pos_1st_dot])

        return url[:num_pos_1st_dot].lstrip("http://")


url = "http://github.com/carbonfive/raygun"
# url = "http://www.zombie-bites.com"
res = domain_name(url)
print(res)