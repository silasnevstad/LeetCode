class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest_price = max(prices)
        max_profit = 0

        for price in prices:
            lowest_price = max(lowest_price, price)
            max_profit = max(max_profit, price - lowest_price)

        return max_profit