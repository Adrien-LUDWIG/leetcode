class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if len(nums) == 0:
            return []
        
        ranges = []

        range_start = 0

        for range_end in range(len(nums) - 1):
            # If the next number directly follows this number, continue
            if nums[range_end + 1] - nums[range_end] == 1:
                continue
                    
            # Else, append the appropriate range representation
            if range_start == range_end:
                ranges.append(str(nums[range_start]))
            else:
                ranges.append(str(nums[range_start]) + "->" + str(nums[range_end]))
            range_start = range_end + 1

        # Add last range
        if range_start == (len(nums) - 1):
            ranges.append(str(nums[-1]))
        else:
            ranges.append(str(nums[range_start]) + "->" + str(nums[-1]))

        return ranges