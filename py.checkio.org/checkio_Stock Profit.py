"""
You are a broker on the stock exchange. You've decided to make just one complete operation: to buy a stock and sell
it later to make a profit. “Short-selling” (sell first, buy later) is not allowed in this market.
Buying and selling prices for every distinct moment are the same (in every moment you may either by a stock for
price x or sell a stock (if you have it) for the same price x) and are shown in the given list stock.
So, you have to choose, what are the best prices to buy a stock and later sell it to make the maximum profit from
the operation. Your function must return this maximum possible profit. If it's not possible to make any profit with
given prices (it's <= 0), your function should return 0.
Input: Stock prices as list of integers.
Output: Maximum possible profit as integer.
"""
def stock_profit(stock):
    # index = stock.index(min(stock))
    # if len(stock) == index + 1:
    #     return 0
    # res = max(stock[index+1:]) - min(stock)
    # return res

    prof = 0
    l = len(stock)
    for b_ind in range(l - 1):
        for s_ind in range(b_ind + 1, l):
            prof = max(prof, stock[s_ind] - stock[b_ind])

    return prof


stock = [60, 50, 51, 52, 40]
res = stock_profit(stock)
print(res)