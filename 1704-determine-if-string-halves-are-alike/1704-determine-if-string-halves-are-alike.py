def isvowel(char: str):
    return char.lower() in "aeiou"

def count_vowels(s: str):
    return len(list(filter(isvowel, s)))

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        return count_vowels(s[:mid]) == count_vowels(s[mid:])