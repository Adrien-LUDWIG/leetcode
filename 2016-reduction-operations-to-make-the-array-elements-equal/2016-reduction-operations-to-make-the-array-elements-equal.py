class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        operations_count = 0
        last_value = nums[0]

        for index, value in enumerate(nums):
            if value != last_value:
                operations_count += index
                last_value = value
        
        return operations_count
