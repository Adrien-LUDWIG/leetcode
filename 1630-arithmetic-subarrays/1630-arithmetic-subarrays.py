def is_arithmetic(nums: List[int]) -> bool:
    """
    Check if an array is an arithmetic sequence.
    """
    diff = nums[1] - nums[0]

    for i in range(2, len(nums)):
        if (nums[i] - nums[i-1]) != diff:
            return False

    return True

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []

        for left, right in zip(l, r):
            answer.append(is_arithmetic(sorted(nums[left:right+1])))

        return answer 