class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        power = 1

        while power < n:
            power *= 4

        return power == n
        