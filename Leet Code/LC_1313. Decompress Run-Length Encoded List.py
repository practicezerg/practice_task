"""
We are given a list nums of integers representing a list compressed with run-length encoding.
Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair,
there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to
generate the decompressed list.
Return the decompressed list.
"""
def decompressRLElist(nums):
    l= []
    for i in range(int(len(nums)/2)):
        kysok = nums.pop(0)
        value = nums.pop(0)
        for x in range(kysok):
            l.append(value)
    return l






nums = [1,1,2,3]
res = decompressRLElist(nums)
print(res)