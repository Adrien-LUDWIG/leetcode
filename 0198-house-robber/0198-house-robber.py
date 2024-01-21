class Solution:
    def rob(self, nums: List[int]) -> int:
        skipped = 0
        robbed = nums[0]

        for i in range(1, len(nums)):
            skipped, robbed = robbed, max(robbed, skipped + nums[i])

        return robbed
