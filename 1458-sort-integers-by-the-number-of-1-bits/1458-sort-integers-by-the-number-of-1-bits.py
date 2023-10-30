class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # For Python 3.10+ use key = int.bit_count
        return sorted(arr, key=lambda x : (bin(x).count("1"), x))