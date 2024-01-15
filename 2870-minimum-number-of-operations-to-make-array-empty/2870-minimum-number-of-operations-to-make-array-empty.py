from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operation_count = 0
        counter = Counter(nums)
        
        for count in counter.values():
            if count == 1:
                return -1
            operation_count += ceil(count / 3)

        return operation_count