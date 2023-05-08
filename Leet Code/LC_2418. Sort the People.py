"""
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
For each index i, names[i] and heights[i] denote the name and height of the ith person.
Return names sorted in descending order by the people's heights.
"""
def sortPeople(names,heights):
    res, l = {}, []
    for i, x in zip(names, heights):
        res[x] = i
    t = sorted(res.keys(), reverse=True)
    for i in t:
        l.append(res[i])
    return l




names = ["Mary","John","Emma"]
heights = [180,165,170]
res =  sortPeople(names, heights)
print(res)