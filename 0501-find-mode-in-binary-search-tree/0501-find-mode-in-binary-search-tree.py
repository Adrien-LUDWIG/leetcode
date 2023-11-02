from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            """
            Given a Binary Search Tree, create a sorted list of values.
            Create the inorder traversal list.
            """
            nonlocal modes, current_value, count, max_count

            if root is None:
                return

            dfs(root.left)

            if root.val == current_value:
                count += 1
            else:
                current_value = root.val
                count = 1

            # If this is the most seen value
            if max_count < count:
                # Reset the list of modes to contain this value only
                modes = [root.val]
                max_count = count
            elif max_count == count:
                modes.append(root.val)

            dfs(root.right)


        # Create sorted list of values
        modes = []
        max_count = 0
        current_value = 0
        count = 0

        dfs(root)

        return modes