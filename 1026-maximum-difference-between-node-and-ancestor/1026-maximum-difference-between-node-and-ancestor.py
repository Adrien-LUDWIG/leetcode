# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def max_ancestor_diff(node, low=float("inf"), high=0):
    if not node:
        return 0
    low = min(low, node.val)
    high = max(high, node.val)
    return max(high - low, max(max_ancestor_diff(node.left, low, high), max_ancestor_diff(node.right, low, high)))

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return max_ancestor_diff(root)