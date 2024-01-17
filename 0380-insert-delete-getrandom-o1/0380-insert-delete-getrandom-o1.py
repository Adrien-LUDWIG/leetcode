class RandomizedSet:
    def __init__(self):
        self._values = []
        self._indices = {}

    def insert(self, val: int) -> bool:
        if val in self._indices:
            return False

        self._indices[val] = len(self._values)
        self._values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._values:
            return False

        # Replace val by last element (or itself if it is the last element)
        self._indices[self._values[-1]] = self._indices[val]
        self._values[self._indices[val]] = self._values[-1]

        # Remove last element
        self._values.pop()
        self._indices.pop(val)

        return True

    def getRandom(self) -> int:
        return self._values[randint(0, len(self._values) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
