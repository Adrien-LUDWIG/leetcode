from collections import defaultdict

MODULO = int(1e9) + 7

def reverse_digits(n: int) -> int:
    """
    Reverses the digits of the given postive integer.
    """
    return int(str(n)[::-1])

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        diff_num_rev = defaultdict(int)
        count_nice_pairs = 0

        for i in range(len(nums)):
            diff = nums[i] - reverse_digits(nums[i])
            count_nice_pairs = (count_nice_pairs + diff_num_rev[diff]) % MODULO
            diff_num_rev[diff] += 1

        return count_nice_pairs