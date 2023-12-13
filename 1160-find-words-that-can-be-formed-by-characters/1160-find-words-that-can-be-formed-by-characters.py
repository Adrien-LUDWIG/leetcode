from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)        

        good_length_sum = 0

        for word in words:
            word_chars_count = Counter(word)

            if all(word_chars_count[char] <= chars_count[char] for char in word_chars_count):
                good_length_sum += len(word)
            
        return good_length_sum
                