"""
We have a list of booleans. Let's check if the majority of elements are True.
Some cases worth mentioning: 1) an empty list should return False; 2) if True-s and False-s have an equal amount,
function should return False.
"""
def is_majority(items):
    if items.count(True) > items.count(False):
        return True
    return False


items = [True, True, False, True, False]
res = is_majority(items)
print(res)