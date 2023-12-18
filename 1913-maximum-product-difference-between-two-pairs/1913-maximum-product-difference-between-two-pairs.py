INF = float("inf")

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min1 = INF
        min2 = INF
        max1 = 0
        max2 = 0

        for num in nums:
            if num < min2:
                if num < min1:
                    min2 = min1
                    min1 = num
                else:
                    min2 = num
            if num > max2:
                if num > max1:
                    max2 = max1
                    max1 = num
                else:
                    max2 = num
        
        return max1 * max2 - min1 * min2