class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def longestPalindrome(start, end):
            """
            Expand the current palindrome until it's not a palindrome anymore.
            """
            while 0 <= start and end < n and s[start] == s[end]:
                start -= 1
                end += 1
            return start + 1, end - 1
        
        n = len(s)
        
        if n == 1:
            return s
        
        max_length = -1
        best_start = -1
        best_end = -1
        
        # Loop over the string
        for index in range(n - 1):
            # For each position, check odd and even palindromes
            for offset in (0, 1):
                # Find the longest palindrome centered on this index
                start, end = longestPalindrome(index, index + offset)
                length = end - start + 1
                
                # Keep track of the longest palindrome
                if max_length < length:
                    max_length = length
                    best_start = start
                    best_end = end

        return s[best_start:best_end+1]
