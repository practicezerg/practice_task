"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the
i​​​​​​​​​​​th​​​​ customer has in the
j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer
that has the maximum wealth.
"""
def maximumWealth(accounts):
    l_sum = []
    for i in accounts:
        l_sum.append(sum(i))
    return max(*[l_sum])



accounts = [[1,5],[7,3],[3,5]]
res = maximumWealth(accounts)
print(res)