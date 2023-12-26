from functools import cache

MODULO = int(1e9) + 7

class Solution:
    def numRollsToTarget(self, dice_count: int, face_count: int, target: int) -> int:

        @cache
        def rec(dice_count, target):
            if target < dice_count or target > dice_count * face_count:
                return 0
            if dice_count == 1:
                return 1
            
            combination_count = 0

            for face in range(1, face_count + 1):
                combination_count += rec(dice_count - 1, target - face)
                combination_count %= MODULO
            
            return combination_count
        
        return rec(dice_count, target)