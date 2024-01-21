class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def rec(index=0):
            if index >= len(nums):
                return 0

            rob = nums[index] + rec(index + 2)
            skip = rec(index + 1)
            return max(rob, skip)

        return rec()
