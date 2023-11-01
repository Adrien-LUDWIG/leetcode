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
            if root is None:
                return
            
            occurrencies[root.val] += 1
            dfs(root.left)
            dfs(root.right)

        occurrencies = defaultdict(int)

        dfs(root)

        max_occurrencies = max(occurrencies.values())
        modes = [key for key, value in occurrencies.items() if value == max_occurrencies]

        return modes