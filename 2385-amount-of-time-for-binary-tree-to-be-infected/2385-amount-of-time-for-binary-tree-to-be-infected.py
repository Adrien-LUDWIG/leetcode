# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def add_parents(tree, parent=None):
    if not tree:
        return 
    tree.parent = parent
    add_parents(tree.left, tree)
    add_parents(tree.right, tree)


def get_subtree(tree, subroot):
        if not tree:
            return
        if tree.val == subroot:
            return tree
        return get_subtree(tree.left, subroot) or get_subtree(tree.right, subroot)
    
def infection_time(node, src=None):
    if not node:
        return -1
    max_time = -1
    
    for neighbor in (node.parent, node.left, node.right):
        if neighbor != src:
            max_time = max(max_time, infection_time(neighbor, node))
    
    return max_time + 1
    
        
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        add_parents(root)
        start_node = get_subtree(root, start)
        return infection_time(start_node)