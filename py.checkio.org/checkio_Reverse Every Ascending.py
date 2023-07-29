"""
Create and return a new Iterable that contains the same elements as the argument list items, but with the reversed order
of the elements inside every maximal strictly ascending subsequence. This function should not modify the contents of
the original list.
Input: List of integers.
Output: List or another Iterable (tuple, iterator, generator) of integers.
"""
def reverse_ascending(items):
    if items:
        l = [items[0]]
        res = []
        n = 0
        for num in items[1:]:
            if num > items[n]:
                l.append(num)
                n += 1
            else:
                l = sorted(l, reverse=True)
                res.extend(l)
                l = []
                l.append(num)
                n += 1
        if l:
            l = sorted(l, reverse=True)
            res.extend(l)
        return res
    else:
        return items




items = []
res = reverse_ascending(items)
print(res)