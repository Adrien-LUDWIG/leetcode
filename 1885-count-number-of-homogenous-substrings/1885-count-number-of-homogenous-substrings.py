MODULO = int(1e9 + 7)

class Solution:
    def countHomogenous(self, s: str) -> int:
        total = 0
        local = 0
        last_char = None
        
        for char in s:
            if char != last_char:
                last_char = char
                local = 0
            local += 1
            total = (total + local) % MODULO
        
        return total