# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0, 0, 0

            nodes_sum_left, nodes_count_left, count_average_left = dfs(root.left)
            nodes_sum_right, nodes_count_right, count_average_right = dfs(root.right)

            nodes_sum = root.val + nodes_sum_left + nodes_sum_right
            nodes_count = 1 + nodes_count_left + nodes_count_right

            count_average = count_average_left + count_average_right

            if nodes_sum // nodes_count == root.val:
                count_average += 1

            return nodes_sum, nodes_count, count_average

        _, _, count_average = dfs(root)

        return count_average