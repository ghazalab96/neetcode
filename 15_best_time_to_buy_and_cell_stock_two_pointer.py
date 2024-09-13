from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        l, r = 0, 1  # l = buy, r = sell
        
        while r < len(prices):  # we can keep going until the right pointer is on the end point of the list
            if prices[l] < prices[r]:  # we can make profit here
                profit = prices[r] - prices[l]
                max_p = max(max_p, profit)

            else:  # if price[l] >= price [r] means that we have founf another selling point lower than the last left point.
                l = r
            r += 1 # right point moves constantly to find the highest price to sell the stock
        return max_p
        