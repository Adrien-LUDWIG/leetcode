class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        return [v for _, _, v in sorted([(i+j, j, value) for i, row in enumerate(nums) for j, value in enumerate(row)])]
        