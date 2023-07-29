"""Your job here is to write a function (keepOrder in JS/CoffeeScript, keep_order in Ruby/Crystal/Python,
keeporder in Julia), which takes a sorted array ary and a value val, and returns the lowest index where you could
insert val to maintain the sorted-ness of the array. The input array will always be sorted in ascending order.
It may contain duplicates."""

def keep_order(ary, val):
    for i in ary:
        if i >= val:
            get_index = ary.index(i)
            ary.insert(get_index, val)
            return get_index
    return len(ary)

ary = [1, 2, 3, 4, 7]
val = 5
res = keep_order(ary, val)
print(res)