class RandomizedSet:

    def __init__(self):
        self._values = []
        self._values_indices = {}

    def insert(self, val: int) -> bool:
        if val in self._values_indices:
            return False

        self._values_indices[val] = len(self._values)
        self._values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._values:
            return False

        last_val = self._values.pop()
        self._values_indices[last_val] = self._values_indices.pop(val)
        self._values[self._values_indices[last_val]] = last_val
        return True

    def getRandom(self) -> int:
        return self._values[randint(0, len(self._values) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()