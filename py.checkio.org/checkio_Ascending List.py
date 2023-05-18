"""
Determine whether the list of elements is ascending such that each of its elements is strictly larger than
(and not merely equal to) the preceding element. Empty list consider as ascending.
Input: A list with integers.
Output: Boolean.
"""
def is_ascending(items):
    num = 0
    for i in items[1:]:
        print(i, num)
        if i <= items[num]:
            return False
        num +=1
    return True



items = [1, 1, 1, 1]
res = is_ascending(items)
print(res)