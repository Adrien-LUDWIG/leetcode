import re

class Solution:
    def largestOddNumber(self, num: str) -> str:
        last_odd_digit_index = len(num) - 1

        while last_odd_digit_index >= 0 and int(num[last_odd_digit_index]) % 2 != 1:
            last_odd_digit_index -= 1
        return  num[:last_odd_digit_index + 1]
        