class RandomizedSet:

    def __init__(self):
        self._values = set()
        

    def insert(self, val: int) -> bool:
        seen = val in self._values
        self._values.add(val)
        return not seen

    def remove(self, val: int) -> bool:
        seen = val in self._values
        self._values.discard(val)
        return seen
        

    def getRandom(self) -> int:
        return list(self._values)[randint(0, len(self._values) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()