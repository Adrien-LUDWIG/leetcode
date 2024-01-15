from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operation_count = 0
        counter = Counter(nums)
        
        for count in counter.values():
            while count != 0:
                
                if count > 4 or count == 3:

                    count -= 3
                elif count == 2 or count == 4:

                    count -= 2
                else:
                    return -1
                
                operation_count += 1

        
        return operation_count