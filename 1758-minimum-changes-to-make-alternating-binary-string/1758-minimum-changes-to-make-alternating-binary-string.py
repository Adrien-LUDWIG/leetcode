class Solution:
    def minOperations(self, s: str) -> int:
        zero_first = 0
        one_first = 0
        alternating_bit = "0"
        
        for bit in s:
            zero_first += bit != alternating_bit
            one_first += bit == alternating_bit
            alternating_bit = "0" if alternating_bit == "1" else "1"
            
        return min(zero_first, one_first)