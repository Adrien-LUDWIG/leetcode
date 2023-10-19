class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Point of view that unlocked the problem for me:
        # The problem is similar to caclulating the ascent for a hiking path.
        # The max profit is equal to all the cumulative price increases.

        max_profit = 0
        # We need to start by buying to be able to sell
        buying_price = prices[0]

        for i in range(1, len(prices)):
            # We update our buying price if we find better
            buying_price = min(buying_price, prices[i])

            # If it's the last day or stock value is about to fall, we sell
            if i == len(prices) - 1 or prices[i] > prices[i+1]:
                max_profit += prices[i] - buying_price
                # Again, we need to buy if we want to be able to sell
                buying_price = prices[i]

        return max_profit
        