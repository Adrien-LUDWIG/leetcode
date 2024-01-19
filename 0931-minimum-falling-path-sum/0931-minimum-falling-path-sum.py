class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        height, width = len(matrix), len(matrix[0])
        line = matrix[0]

        for i in range(1, height):
            new_line = [float("inf")] * width

            for j in range(width):
                for j_ in range(max(0, j-1), min(width, j+2)):
                    new_line[j] = min(new_line[j], line[j_] + matrix[i][j])
            
            line = new_line
        
        return min(line) 
