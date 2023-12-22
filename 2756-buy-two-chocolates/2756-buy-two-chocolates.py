def min_pair(nums):
    min1 = min2 = float("inf")
    
    for n in nums:
        if n < min2:
            if n < min1:
                min2 = min1
                min1 = n
            else:
                min2 = n
    return min1, min2

class Solution(object):
    def buyChoco(self, prices: List[int], money: int) -> int:
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        

        money_left = money - sum(min_pair(prices))
        return money_left if money_left >= 0 else money