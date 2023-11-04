class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if not left:
            return n - min(right)
        if not right:
            return max(left)

        return max(n - min(right), max(left))