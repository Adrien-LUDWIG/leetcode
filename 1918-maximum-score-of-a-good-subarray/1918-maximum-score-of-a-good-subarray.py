class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = k
        j = k
        min_value = nums[k]
        max_score = nums[k]

        while i > 0 or j < len(nums) - 1:
            while i > 0 and nums[i - 1] >= min_value:
                i -= 1
            while j < len(nums) - 1 and nums[j + 1] >= min_value:
                j += 1

            max_score = max(max_score, min_value * (j - i + 1))

            if i > 0 and j < len(nums) - 1:
                if nums[i - 1] >= nums[j + 1]:
                    i -= 1
                    min_value = nums[i]
                else:
                    j += 1
                    min_value = nums[j]
            elif i > 0:
                i -= 1
                min_value = nums[i]
            elif j < len(nums) - 1:
                j += 1
                min_value = nums[j]

            max_score = max(max_score, min_value * (j - i + 1))

        return max_score 