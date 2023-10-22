from collections import deque

class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sub_sums = [nums[0]]

        # Max of sub_sums
        max_sub_sum = sub_sums[0]

        # Max of the last k sub_sums
        sliding_max = deque()
        sliding_max.append(sub_sums[0])


        for i in range(1, len(nums)):
            new_sub_sum = nums[i] + max(0, sliding_max[0])
            sub_sums.append(new_sub_sum)

            # Update sliding window max
            # Remove too small values
            while sliding_max and sliding_max[-1] < new_sub_sum:
                sliding_max.pop()
            # Append new value
            sliding_max.append(new_sub_sum)
            # Remove sliding window leftmost value
            # (which will leave the sliding window in next loop)
            if i >= k and sliding_max[0] == sub_sums[i - k]:
                sliding_max.popleft()

            max_sub_sum = max(max_sub_sum, new_sub_sum)

        return max_sub_sum