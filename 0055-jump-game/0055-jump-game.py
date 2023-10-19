class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        visitable_indices = [False] * len(nums)
        # We always start from the first index
        visitable_indices[0] = True

        for i in range(len(nums) - 1):
            # Turn all indices visitable from here to True
            visitable_indices[i+1:i+1+nums[i]] = [True] * nums[i]
        
        return all(visitable_indices)