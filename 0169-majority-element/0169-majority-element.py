class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Return the median
        return sorted(nums)[len(nums)/2]