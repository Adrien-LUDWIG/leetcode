class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        # If the array is empty, there is no range
        if len(nums) == 0:
            return []
        
        ranges = []
        range_start = 0

        for range_end in range(len(nums)):
            # If we're at the end of the list or if numbers aren't consecutive
            if range_end == len(nums) - 1 or nums[range_end + 1] - nums[range_end] != 1:
                # Add a new range to the list
                if range_start == range_end:              # Only one number
                    ranges.append(str(nums[range_start]))
                else:                                     # Multiple numbers
                    ranges.append(str(nums[range_start]) + "->" + str(nums[range_end]))
                range_start = range_end + 1

        return ranges