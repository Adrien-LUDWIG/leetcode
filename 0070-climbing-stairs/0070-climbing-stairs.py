class Solution:
    def climbStairs(self, n: int) -> int:
        odd = 1
        even = 1

        for _ in range(n // 2):
            odd += even
            even += odd

        return even if n % 2 else odd
