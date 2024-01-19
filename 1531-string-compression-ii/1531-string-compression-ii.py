class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def rec(index=0, prev_char=None, char_count=0, k=k):
            if k < 0:
                return float("inf")
            if index == len(s):
                return 0
            # Always accept same chars since deny is done in the else
            if s[index] == prev_char:
                char_count += 1
                new_digit = char_count == 2 or log(char_count, 10).is_integer()
                accept = rec(index+1, prev_char, char_count, k)
                return accept + new_digit
            else: # s[index] != prev_char
                accept = 1 + rec(index+1, s[index], 1, k)
                deny = rec(index+1, prev_char, char_count, k-1)
                return min(accept, deny)
        
        return rec()