class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles, reverse=True)[1:len(piles)//3 * 2:2])