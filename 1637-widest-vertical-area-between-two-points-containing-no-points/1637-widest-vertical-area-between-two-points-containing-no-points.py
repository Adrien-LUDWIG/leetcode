class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points_abscissas = [x for x, y in points]
        points_abscissas.sort()
        steps = [b - a for a, b in zip(points_abscissas[:-1], points_abscissas[1:])]
        return max(steps)