# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root):
            if root is None:
                return
            
            if root.val in occurrencies:
                occurrencies[root.val] += 1
            else:
                occurrencies[root.val] = 1
            
            dfs(root.left)
            dfs(root.right)

        occurrencies = {}

        dfs(root)

        max_occurrencies = max(occurrencies.values())
        modes = [key for key, value in occurrencies.items() if value == max_occurrencies]

        return modes
