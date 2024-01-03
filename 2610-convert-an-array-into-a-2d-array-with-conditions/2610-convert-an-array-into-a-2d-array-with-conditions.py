from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        array = [[] for _ in range(counter.most_common(1)[0][1])]
        
        for letter, count in counter.items():
            for index in range(count):
                array[index].append(letter)
               
        return array
        