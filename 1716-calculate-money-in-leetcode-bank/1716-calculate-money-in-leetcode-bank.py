COMPLETE_WEEK_MONEY = sum(range(8))

class Solution:
    def totalMoney(self, n: int) -> int:

        complete_weeks = n // 7
        remaining_days = n % 7

        money = complete_weeks * COMPLETE_WEEK_MONEY + sum(range(complete_weeks)) * 7
        money += sum(range(remaining_days + 1)) + complete_weeks * remaining_days
            
        return money


            