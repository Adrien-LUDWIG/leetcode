from collections import deque

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
        
        queue = deque()
        queue.append(root)
        max_rows = []
        max_row = float("-inf")

        while queue:
            n = len(queue)
            for _ in range(n):
                root = queue.popleft()
                if root:
                    max_row = max(max_row, root.val)
                    queue.append(root.left)
                    queue.append(root.right)

            if max_row != float("-inf"):
                max_rows.append(max_row)
                max_row = float("-inf")
        
        return max_rows


