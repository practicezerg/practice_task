"""
You have a lot of work to do, so you might want to split it into smaller pieces. This way you'll know which piece you'll
do on Monday, which will be for Tuesday and so on.
Split a list into smaller lists of the same size (chunks). The last chunk can be smaller than the default chunk-size.
If the list is empty, then you shouldn't have any chunks at all.
"""
def chunking_by(items, size):
    count = 0
    res, l = [], []
    for i in items:
        l.append(i)
        count += 1
        if count == size:
            res.append(l)
            l, count =[], 0
    if l:
        res.append(l)
    return res





items, size = [5, 4, 7, 3, 4, 5, 4], 3
res = chunking_by(items, size)
print(res)