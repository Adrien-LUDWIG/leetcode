class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        height, width = len(grid), len(grid[0])

        rows_sum = [0] * height
        cols_sum = [0] * width

        for i in range(height):
            for j in range(width):
                rows_sum[i] += grid[i][j]
                cols_sum[j] += grid[i][j]

        diff = [[0] * width for _ in range(height)]

        for i in range(height):
            for j in range(width):
                row_zeros = width - rows_sum[i]
                col_zeros = height - cols_sum[j]
                diff[i][j] = rows_sum[i] + cols_sum[j] - row_zeros - col_zeros
        
        return diff