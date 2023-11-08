class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []

        max_value = target[-1]
        value = 1
        index = 0

        while value <= max_value:
            operations.append("Push")

            if value != target[index]:
                operations.append("Pop")
            else:
                index +=1

            value += 1
        
        return operations