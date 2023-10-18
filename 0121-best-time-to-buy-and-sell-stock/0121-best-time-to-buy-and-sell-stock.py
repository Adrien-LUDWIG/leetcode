def max_with_index(array, slice_offset=0):
    array = array[slice_offset:]

    max_value = array[-1]
    max_index = len(array) - 1

    index = len(array) - 1
    while index >= 0:
        if array[index] > max_value:
            max_value = array[index]
            max_index = index
        index -= 1
    
    return max_value, max_index + slice_offset
    

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) < 2:
            return 0

        max_sell_price, max_sell_index = max_with_index(prices, 1)
        min_buy_price = min(prices[:max_sell_index])
        max_profit = max(0, max_sell_price - min_buy_price)

        while max_sell_index < len(prices) - 2:
            max_sell_price, new_max_sell_index = max_with_index(prices, max_sell_index+2)

            if max_sell_price <= max_profit:
                break

            print(max_sell_index, new_max_sell_index)
            min_buy_price = min(prices[max_sell_index+1:new_max_sell_index])

            max_profit = max(max_profit, max_sell_price - min_buy_price)

            max_sell_index = new_max_sell_index 

        return max_profit




