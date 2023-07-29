"""Your function should create a list of lists, that represents a two-dimensional grid with the given number of rows and cols.
This grid should contain the integers from start to start + rows * cols - 1 in ascending order, but the elements of every odd-index row have to be listed in descending order, so that when read in ascending order, the numbers zigzag through the two-dimensional grid.
Input: Two integers - rows and columns. One optional integer - start.
Output: List of lists."""

def create_zigzag(rows, cols, start=1):
    print(rows, cols, start)
    res, l = [], []
    list_test = []
    count = 0
    if cols == 0 and rows == 0:
        return []
    if cols == 0:
        return [[], [], []]
    l = [i for i in range(start, start+(rows*cols))]

    for i in l:
        count += 1
        list_test.append(i)
        if count == cols:
            res.append(list_test)
            list_test = []
            count = 0
    for i in res:
        if res.index(i) % 2 != 0:
            pos = res.index(i)
            rev_pos = sorted(i, reverse=True)
            res.pop(pos)
            res.insert(pos, rev_pos)
    return res


rows, cols  = 4, 5
res = create_zigzag(rows, cols)
print(res)