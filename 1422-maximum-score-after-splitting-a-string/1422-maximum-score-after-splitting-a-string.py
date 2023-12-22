class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        left_score = 0
        right_score = s.count("1")
        
        for bit in s[:-1]: 
            left_score += bit == "0"
            right_score -= bit == "1"
            max_score = max(max_score, left_score + right_score) 
        
        return max_score

