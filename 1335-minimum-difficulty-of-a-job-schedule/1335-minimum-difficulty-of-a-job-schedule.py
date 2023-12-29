from functools import cache

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @cache
        def rec(index, max_day, left_days):
            if left_days == -1 or len(jobDifficulty) - index < left_days:
                return float("inf")
            if index == len(jobDifficulty) and left_days == 0:
                return max_day

            same_day = rec(index + 1, max(jobDifficulty[index], max_day), left_days)
            new_day = max_day + rec(index + 1, jobDifficulty[index], left_days - 1)
            
            return min(same_day, new_day)
                
        min_difficulty = rec(1, jobDifficulty[0], d-1)
        return min_difficulty if min_difficulty != float("inf") else -1
