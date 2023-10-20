# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == [-1] and inorder == [-1]:
            return TreeNode(-1)

        def recBuildTree(preorder, inorder):
            if not preorder:
                return None, preorder, inorder
    
            root = TreeNode(preorder[0])
            preorder = preorder[1:]
    
            if inorder[0] != root.val:
                root.left, preorder, inorder = recBuildTree(preorder, inorder)
            # inorder[0] must be equal to root.val now, we can ignore it
            inorder = inorder[1:]
            if inorder and  inorder[0] in preorder:
                root.right, preorder, inorder = recBuildTree(preorder, inorder)
    
            return root, preorder, inorder

        root, _, _ = recBuildTree(preorder, inorder)

        return root