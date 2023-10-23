class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums)
        mid = left + (right - left) // 2

        while left != right and nums[mid] != target:
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
            mid = left + (right - left) // 2
            
        if left == right:
            return left
        return mid