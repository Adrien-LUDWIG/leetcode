DIRECTIONS = {
    "N": complex(-1, 0),
    "W": complex(0, -1),
    "S": complex(1, 0),
    "E": complex(0, 1),
}

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        position = complex(0, 0)
        visited = set([position])

        for direction in path:
            position += DIRECTIONS[direction]

            if position in visited:
                return True
            
            visited.add(position)
        
        return False

        