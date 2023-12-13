class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        existing_values = set()
        
        for num in nums:
            existing_values.add(int(num, 2))
        
        value = 0
        while value in existing_values:
            value += 1

        return f"{value:b}".zfill(len(nums))