class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)

        # Sort jobs by end time
        jobs = sorted(zip(endTime, startTime, profit))
        endTime = [job[0] for job in jobs]

        # Find the best possible profit
        dp = [0] * (n + 1)

        for i, (end, start, profit) in enumerate(jobs, start=1):
            last_compatible = bisect_right(endTime, start, hi=i)
            dp[i] = max(profit + dp[last_compatible], dp[i - 1])
        
        return dp[-1]