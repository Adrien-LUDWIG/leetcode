class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)

        # Sort jobs by end time
        jobs = sorted(zip(endTime, startTime, profit))

        # Find the best possible profit
        dp = [0]
        ends = []

        for end, start, profit in jobs:
            # Find last compatible job to test if the current one should be kept
            last_compatible = bisect_right(ends, start)
            total_profit = profit + dp[last_compatible]
            
            # If keeping this job is the new best choice, add it to the possibilities
            if total_profit > dp[-1]:
                dp.append(total_profit)
                ends.append(end)
        
        return dp[-1]