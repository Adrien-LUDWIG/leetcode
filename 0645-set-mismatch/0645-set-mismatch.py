class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        expected_range = range(1, len(nums) + 1)

        dupplicated = counter.most_common(1)[0][0]
        [missing] = expected_range - counter.keys()

        return [dupplicated, missing]
