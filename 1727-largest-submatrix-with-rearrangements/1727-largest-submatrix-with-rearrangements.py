class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        for col in range(n):
            for row in range(1, m):
                if matrix[row][col]:
                    matrix[row][col] += matrix[row-1][col]
        
        max_area = 0
                
        for row in matrix:
            row.sort(reverse=True)
            width = 0
            
            while width < n and row[width] > 0:
                max_area = max(max_area, (width + 1) * row[width])
                width += 1
            
        return max_area
