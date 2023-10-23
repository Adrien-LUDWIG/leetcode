# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def rec(nums):
            if not nums:
                return None
            
            mid = len(nums)//2
            return TreeNode(nums[mid], rec(nums[:mid]), rec(nums[mid + 1:]))

        return rec(nums)