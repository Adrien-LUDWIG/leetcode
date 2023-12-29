class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        total_time = 0
        
        last_color = None
        max_time = 0
        sum_time = 0
        
        for color, time in zip(colors, neededTime):
            if color != last_color:
                total_time += sum_time - max_time
                last_color = color
                max_time = time
                sum_time = time
            else: # color == last_color
                max_time = max(time, max_time)
                sum_time += time 
        total_time += sum_time - max_time
        return total_time