class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def rec(n):
            if n < 2:
                return 1
            return rec(n-2) + rec(n-1)
        
        return rec(n)