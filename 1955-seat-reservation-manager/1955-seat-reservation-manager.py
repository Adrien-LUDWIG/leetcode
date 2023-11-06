from heapq import heappush, heappop

class SeatManager:
    def __init__(self, n: int):
        self._available_seats = []

        for seat_number in range(1, n + 1):
            heappush(self._available_seats, seat_number)

    def reserve(self) -> int:
        return heappop(self._available_seats)
        # Reserve seat

    def unreserve(self, seat_number: int) -> None:
        heappush(self._available_seats, seat_number)
        
# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)