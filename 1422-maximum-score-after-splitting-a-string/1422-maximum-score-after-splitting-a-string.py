class Solution:
    def maxScore(self, s: str) -> int:
        left_zeros = 0
        right_ones = len(s) - (s[-1] == "0")
        score = right_ones - (s[0] == "1")
        
        for bit in s[:-1]: 

            right_ones -= 1

            if bit == "0":
                left_zeros += 1
                score = max(score - 1, left_zeros + right_ones)
            
        return score

