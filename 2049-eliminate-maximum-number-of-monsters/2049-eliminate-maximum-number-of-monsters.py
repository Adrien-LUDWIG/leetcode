from heapq import heapify, heappop

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        # Time to kill each monster
        time = []

        for d, s in zip(dist, speed):
            # Time = Distance / Speed
            time.append(d / s)

        # Sort to know in which order to kill monsters
        heapify(time)

        # The number of shots is equal to the number of monsters killed
        shots = 0

        # While we have time to kill a monster, keep shooting
        while time and shots < heappop(time):
            shots += 1
        
        return shots
