"""
Not all of the elements are important. What you need to do here is to remove all of the elements after the given one
from list.
example
For illustration, we have a list [1, 2, 3, 4, 5] and we need to remove all the elements that go after 3 - which is 4 and 5.
We have two edge cases here:
if a cutting element cannot be found, then the list shouldn't be changed;
if the list is empty, then it should remains empty.
Input: List of integers and the border element integer.
Output: List or other Iterable (tuple, iterator, generator ...) of integers.
"""
def remove_all_after(items, border):
    l = []
    for i in items:
        l.append(i)
        if i == border:
            break
    return l


items = [7,7,7,7,7,7]
border = 7
res = remove_all_after(items, border)
print(res)