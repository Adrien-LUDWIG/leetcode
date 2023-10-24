class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        step1 = 1
        step2 = 2

        for _ in range(n-1):
            step1, step2 = step2, step1 + step2

        return step1