class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        max_pair_sum = -1

        start = 0
        end = len(nums) - 1

        while start < end:
            max_pair_sum = max(max_pair_sum, nums[start] + nums[end])
            start += 1
            end -= 1
        
        return max_pair_sum