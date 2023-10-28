class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindrome(s):

            return s == s[::-1]
        
        n = len(s)
        
        for length in range(n, 1, -1):
            for i in range(n - length + 1):
                if isPalindrome(s[i:i+length]):
                    return s[i:i+length]


        return s[0]
