def last_max_index(array, value):
    array.reverse()
    index = array.index(value)
    array.reverse()
    return len(array) - index - 1 


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_sell_index = 0
        max_profit = 0

        while max_sell_index < len(prices) - 1:
            max_sell_price = max(prices[max_sell_index+1:])

            if max_sell_price <= max_profit:
                break

            new_max_sell_index = last_max_index(prices, max_sell_price)

            min_buy_price = min(prices[max_sell_index:new_max_sell_index])

            new_max_profit = max_sell_price - min_buy_price

            if new_max_profit > max_profit:
                max_profit = new_max_profit

            max_sell_index = new_max_sell_index 

        return max_profit




