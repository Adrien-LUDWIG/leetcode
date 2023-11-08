class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for index, value in enumerate(nums):

            complementary = target - value

            if complementary in values:
                return (values[complementary], index)
            else: 
                values[value] = index