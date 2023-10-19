def recMaxProfit(prices, day, has_action=False):
    if day == len(prices):
        return 0 # No more action possible

    # Wait and see until the next day
    do_nothing = recMaxProfit(prices, day + 1, has_action=has_action)

    if has_action: # Sell
        sell = prices[day] + recMaxProfit(prices, day + 1, has_action=False)
        return max(do_nothing, sell)
    else: # Buy
        buy = -prices[day] + recMaxProfit(prices, day + 1, has_action=True)
        return max(do_nothing, buy)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # The problem is similar to caclulating the ascent for a hiking path

        max_profit = 0
        # We need to start by buying to be able to sell
        buying_price = prices[0]

        for i in range(1, len(prices)):
            # But we keep looking for the best price to buy
            buying_price = min(buying_price, prices[i])

            # If it's the last day or stock value is about to fall, we sell
            if i == len(prices) - 1 or prices[i] > prices[i+1]:
                max_profit += prices[i] - buying_price
                # Again, we need to buy if we want to be able to sell
                buying_price = prices[i]

        return max_profit
        