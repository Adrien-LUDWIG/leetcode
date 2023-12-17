from collections import defaultdict
from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self._food_rating  = {} # food : rating
        self._food_cuisine = {} # food : cuisine
        self._cuisine_ratings = defaultdict(SortedSet) # cuisine -> (rating, food)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self._food_cuisine[food] = cuisine
            self._food_rating[food] = rating
            self._cuisine_ratings[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating = self._food_rating[food]
        self._food_rating[food] = newRating

        cuisine = self._food_cuisine[food]
        self._cuisine_ratings[cuisine].discard((-oldRating, food))
        self._cuisine_ratings[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self._cuisine_ratings[cuisine][0][1]
