class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort(reverse=True)

        left = max_frequency = curr_frequency = 0
        used_operations = 0

        for right in range(n):

            used_operations += nums[left] - nums[right]
            curr_frequency += 1

            if used_operations <= k:
                max_frequency = max(max_frequency, curr_frequency)

            while left < right and used_operations > k:
                used_operations -= (nums[left] - nums[left + 1]) * (curr_frequency - 1)
                left += 1
                curr_frequency -= 1
            
        return max_frequency
