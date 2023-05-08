"""A given list should be "compressed" in a way so, instead of two (or more) equal elements, staying one after another,
there should be only one in the result Iterable (list, tuple, iterator, generator).
example
Input: A list.
Output: "Compressed" List or another Iterable (tuple, iterator, generator)."""

def compress(items):
    n, l = 0, []
    if len(items):
        l.append(items[0])
        for i in items:
            if i != l[n]:
                l.append(i)
                n += 1
        return l
    else:
        return l


items = [5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0]
res = compress(items)
print(res)