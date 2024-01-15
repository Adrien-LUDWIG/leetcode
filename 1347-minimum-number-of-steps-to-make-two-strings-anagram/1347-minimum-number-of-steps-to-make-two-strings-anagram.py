from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:

        return len(s) - (Counter(s) & Counter(t)).total()
        