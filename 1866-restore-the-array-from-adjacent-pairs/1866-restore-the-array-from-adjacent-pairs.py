from collections import defaultdict 
  
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacentNums = defaultdict(list)
        tips = set()

        for u, v in adjacentPairs:
            adjacentNums[u].append(v)
            adjacentNums[v].append(u)

            for num in (u, v):
                if num in tips:
                    tips.remove(num)
                else:
                    tips.add(num)

        start = tips.pop()

        nums = []
        stack = [start]

        while stack:
            num = stack.pop()

            if not adjacentNums[num]:
                continue

            stack += adjacentNums[num]
            adjacentNums[num] = None
            nums.append(num)

        return nums
        