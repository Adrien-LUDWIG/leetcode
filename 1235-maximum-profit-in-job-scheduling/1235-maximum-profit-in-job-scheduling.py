class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)

        # Sort jobs by end time
        endTime, startTime, profit = map(list, zip(*sorted(zip(endTime, startTime, profit))))

        # Count of jobs that ends before job[i] starts
        end_before = [0] * n

        for i in range(1, n):
            end_before[i] += bisect_right(endTime, startTime[i])

        # Find the best possible profit
        end_before.insert(0, 0)
        profit.insert(0, 0)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = max(profit[i] + dp[end_before[i]], dp[i - 1])
        
        return dp[-1]