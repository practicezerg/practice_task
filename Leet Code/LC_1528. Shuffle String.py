def work(s, indices):
    q = {}
    x = -1
    for i in s:
        q[indices[x+1]] = i
        x+=1
    res = ""
    for i in range(len(s)):
        res = res + q[i]
    return res



s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
res = work(s, indices)
print(res)