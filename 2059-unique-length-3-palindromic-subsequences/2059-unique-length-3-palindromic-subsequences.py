class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        palindroms_count = 0

        for letter in letters:
            start, end = s.index(letter), s.rindex(letter)
            palindroms_count += len(set(s[start+1:end]))

        return palindroms_count