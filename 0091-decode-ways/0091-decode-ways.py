from functools import cache
class Solution:
    @cache
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        if int(s[:2]) <= 26:
            if len(s) == 2:
                return 1 + self.numDecodings(s[1])
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        return self.numDecodings(s[1:])
        