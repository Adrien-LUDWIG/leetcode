# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        def areSymmetric(left, right):
            if left is None or right is None:
                return left is right
            return left.val == right.val and areSymmetric(left.left, right.right) and areSymmetric(left.right, right.left)

        return areSymmetric(root.left, root.right)
        