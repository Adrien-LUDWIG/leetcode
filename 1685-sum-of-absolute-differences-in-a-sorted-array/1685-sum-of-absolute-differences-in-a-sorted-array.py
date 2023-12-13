class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sums = []

        sums.append(sum(nums) - nums[0] * n)

        for i in range(1, n):
            diff = nums[i] - nums[i-1]
            sums.append(sums[i-1] + diff * i - diff * (n - i))

        return sums