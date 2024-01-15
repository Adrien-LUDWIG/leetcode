# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def leaves(tree):
            if tree:

                if not tree.left and not tree.right:
                    yield tree.val
                yield from leaves(tree.left) 
                yield from leaves(tree.right)

        
        return list(leaves(root1)) ==  list(leaves(root2))