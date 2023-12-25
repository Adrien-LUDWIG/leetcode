from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @cache
        def rec(index):
            if index == n:
                return 1
            if s[index] == "0":
                return 0
            if index == n-1:
                return 1
            if int(s[index:index+2]) <= 26:
                return rec(index + 1) + rec(index + 2)
            return rec(index + 1)
        
        return rec(0)
        