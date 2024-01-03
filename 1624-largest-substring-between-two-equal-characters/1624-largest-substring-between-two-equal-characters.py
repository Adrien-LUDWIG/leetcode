from functools import cache

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        @cache
        def rec(left, right):
            if left >= right:
                return -1
            if s[left] == s[right]:
                return right - left - 1
            return max(rec(left + 1, right), rec(left, right - 1))
        
        return rec(0, len(s) - 1)