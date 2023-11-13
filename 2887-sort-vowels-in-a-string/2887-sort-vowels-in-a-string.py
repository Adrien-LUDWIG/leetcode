VOWELS = set("AEIOUaeiou")

class Solution:
    def sortVowels(self, s: str) -> str:
        sorted_vowels_iterator = iter(sorted([char for char in s if char in VOWELS]))
        
        t = []

        for index in range(len(s)):
            if s[index] in VOWELS:
                t.append(next(sorted_vowels_iterator))
            else:
                t.append(s[index])

        return "".join(t)
        