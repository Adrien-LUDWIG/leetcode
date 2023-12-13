class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        max_value = 0

        for value in sorted(arr):
            if value > max_value:
                max_value += 1

        return max_value