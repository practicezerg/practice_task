"""
Sort the integers in a list. But the position of zeros should not be changed.
Input: A list of integers.
Output: A list or another Iterable (tuple, generator, iterator) of integers.
Examples:
assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
"""


def except_zero(items):
    res, sorted_items, n = [], [], 0
    for i in items:
        if i != 0:
            sorted_items.append(i)
    sorted_items = sorted(sorted_items)
    for x in items:
        if x == 0:
            res.append(x)
        else:
            res.append(sorted_items[n])
            n+=1
    return res



items = [0, 2, 3, 1, 0, 4, 5]
res = except_zero(items)
print(res)