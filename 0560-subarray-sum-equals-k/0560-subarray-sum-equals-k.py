class Solution:
    def subarraySum(self, nums: List[int], target: int) -> int:
        sums = {0: 1} # The empty array
        prefix_sum = 0
        count = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            complementary = prefix_sum - target

            if complementary in sums:
                count += sums[complementary]

            sums[prefix_sum] = sums.get(prefix_sum, 0) + 1

        return count
        
        
