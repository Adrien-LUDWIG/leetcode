class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = x
        y = 0

        while n > 0:
            y = y * 10 + n % 10
            n /= 10

        return x == y