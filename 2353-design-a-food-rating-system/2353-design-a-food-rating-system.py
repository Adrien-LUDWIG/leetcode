from collections import defaultdict
from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self._foods = defaultdict(tuple) # food -> (cuisine, rating)
        self._ratings = defaultdict(SortedSet) # cuisine -> (rating, food)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self._foods[food] = (cuisine, rating)
            self._ratings[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, oldRating = self._foods[food]
        self._foods[food] = (cuisine, newRating)
        self._ratings[cuisine].discard((-oldRating, food))
        self._ratings[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self._ratings[cuisine][0][1]
