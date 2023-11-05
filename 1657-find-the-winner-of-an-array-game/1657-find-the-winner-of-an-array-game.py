class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        count = 0
        winner = arr[0]
        first = 0
        second = 1

        while count < k:
            if arr[first] < arr[second]:
                first = second
                winner = arr[first]
                count = 0

            second = (second + 1) % len(arr)
            count += 1

            if second == first:
                return winner
                
        return winner
