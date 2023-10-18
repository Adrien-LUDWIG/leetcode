class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_unseen_value = None
        count = 0
        index = 0

        for value in nums:
            if value != last_unseen_value:
                last_unseen_value = value
                count = 1
                nums[index] = value
                index += 1
            elif count < 2:
                count += 1
                nums[index] = value
                index += 1

        return index