# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return root
        
        queue1 = [root]
        queue2 = []
        max_rows = []
        max_row = float("-inf")

        while queue1:
            while queue1:
                root = queue1.pop(0)

                max_row = max(max_row, root.val)
                if root.left: 
                    queue2.append(root.left)
                if root.right:
                    queue2.append(root.right)

            max_rows.append(max_row)
            max_row = float("-inf")
            queue1, queue2 = queue2, queue1
        
        return max_rows


