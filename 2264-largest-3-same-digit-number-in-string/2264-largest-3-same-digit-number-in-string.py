from re import findall

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        substrings = findall("(000|111|222|333|444|555|666|777|888|999)", num)
        return f'{max(map(int,substrings), default=None):03d}' if substrings else ""