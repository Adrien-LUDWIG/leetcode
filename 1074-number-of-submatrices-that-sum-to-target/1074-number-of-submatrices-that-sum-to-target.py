def subarraySum(prefix_sums: List[int], target: int) -> int:
    sums = {0: 1} # The empty array
    prefix_sum = 0
    count = 0

    for prefix_sum in prefix_sums:
        complementary = prefix_sum - target

        if complementary in sums:
            count += sums[complementary]

        sums[prefix_sum] = sums.get(prefix_sum, 0) + 1

    return count
        
        
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        height, width = len(matrix), len(matrix[0])
        count = 0

        for offset in range(height):
            prefix_sums = [0] * width

            for i in range(offset, height):
                prefix_sum = 0
        
                for j in range(width):
                    prefix_sum += matrix[i][j]
                    prefix_sums[j] += prefix_sum
        
                count += subarraySum(prefix_sums, target)

        
        return count
                
