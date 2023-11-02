from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, values):
            """
            Given a Binary Search Tree, create a sorted list of values.
            Create the inorder traversal list.
            """

            if root is None:
                return

            dfs(root.left, values)
            values.append(root.val)
            dfs(root.right, values)

        # Create sorted list of values
        values = []
        dfs(root, values)

        modes = []
        max_count = 0
        index = 0

        while index < len(values):
            value = values[index]
            start_index = index

            while index < len(values) and values[index] == value:
                index += 1

            count = index - start_index

            # If this is the most seen value
            if max_count < count:
                # Reset the list of modes to contain this value only
                modes = [value]
                max_count = count
            elif max_count == count:
                modes.append(value)
                
        return modes