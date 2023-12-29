from itertools import groupby

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        return sum(sum(grp1) - max(grp2) for grp1, grp2 in (tee(grp) for _, grp in groupby(neededTime, key=lambda _, iter_colors=iter(colors): next(iter_colors))))
