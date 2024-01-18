class Solution:
    def climbStairs(self, n: int) -> int:
        # Possibilities for 0 and 1 stairs
        even = 1 # 0 stairs
        odd = 1 # 1 stairs

        # Climb stairs 2 by 2, counting possibilities
        for _ in range(n // 2):
            even += odd # i * 2 stairs
            odd += even # i * 2 + 1 stairs

        # Return the number of possibilities for n stairs
        return odd if n % 2 else even
