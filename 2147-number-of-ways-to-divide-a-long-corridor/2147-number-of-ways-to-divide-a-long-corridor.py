MODULO = int(1e9) + 7

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        combinations = 1
        count_seats = -2 # Avoid counting plants before first seats
        count_plants = 0

        for index, letter in enumerate(corridor):
            if letter == "S":
                count_seats = (count_seats + 1) % 2
                combinations = (combinations * (count_plants + 1)) % MODULO
                count_plants = 0
            elif count_seats == 0:
                count_plants += 1

        # Even number of seats
        if count_seats != 0:
            return 0
        
        return combinations

                

