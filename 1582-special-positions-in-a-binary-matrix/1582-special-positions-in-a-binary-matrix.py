class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        height, width = len(mat), len(mat[0])
        row_sum = [0] * height
        col_sum = [0] * width

        for i in range(height):
            for j in range(width):
                row_sum[i] += mat[i][j]
                col_sum[j] += mat[i][j]
            
        count = 0
        for i in range(height):
            if row_sum[i] == 1 and col_sum[mat[i].index(1)] == 1:
                count += 1

        return count
