class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_unique_value = None
        index = 0

        # Move the unique values to the beginning of the array
        for value in nums:
            if value != last_unique_value:
                last_unique_value = value
                nums[index] = value
                index += 1

        return index 