from collections import deque

class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sub_sums = [nums[0]]
        max_sub_sum = sub_sums[0]
        sliding_max = deque()
        sliding_max.append(sub_sums[0])


        for i in range(1, len(nums)):
            new_sub_sum = nums[i] + max(0, sliding_max[0])
            sub_sums.append(new_sub_sum)

            if i >= k and sliding_max and sliding_max[0] == sub_sums[i - k]:
                sliding_max.popleft()
            while sliding_max and sliding_max[-1] < new_sub_sum:
                sliding_max.pop()
            sliding_max.append(new_sub_sum)

            max_sub_sum = max(max_sub_sum, new_sub_sum)

        return max_sub_sum