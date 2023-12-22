class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        left_zeros = 0
        right_ones = len(s) - (s[-1] == "0")
        
        for bit in s[:-1]: 

            right_ones -= 1

            if bit == "1":
                score = max(score, left_zeros + right_ones)
            else: # bit == "0"
                left_zeros += 1
                score = max(score - 1, left_zeros + right_ones)
            
        return score

