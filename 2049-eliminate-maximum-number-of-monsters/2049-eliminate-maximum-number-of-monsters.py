from heapq import heappush, heappop

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        # Time to kill each monster
        time = []

        for d, s in zip(dist, speed):
            # Time = Distance / Speed
            heappush(time, d / s)

        # The number of shots is equal to the number of monsters killed
        shots = 0

        # While we have time to kill a monster, keep shooting
        while time and shots < heappop(time):
            shots += 1
        
        return shots
