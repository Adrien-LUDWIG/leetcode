class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrencies = Counter(arr).values()
        return len(occurrencies) == len(set(occurrencies))