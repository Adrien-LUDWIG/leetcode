from collections import defaultdict
from heapq import heappush, heappop

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self._edges = defaultdict(list)

        for src, dst, cost in edges:
            self._edges[src].append((dst, cost))

    def addEdge(self, edge: List[int]) -> None:
        src, dst, cost = edge
        self._edges[src].append((dst, cost))

    def shortestPath(self, src: int, dst: int) -> int:
        
        seen = set()
        nodes_to_visit = [(0, src)] # (total_cost_from_src, node)
        tentative_distances = defaultdict(lambda: float('inf'))
        tentative_distances[src] = 0

        while nodes_to_visit:
            total_cost, node = heappop(nodes_to_visit)

            if node in seen:
                continue

            if node == dst:
                return total_cost

            for neighbor, cost in self._edges[node]:
                if neighbor in seen:
                    continue
                
                new_tentative_distance = total_cost + cost

                if new_tentative_distance < tentative_distances[neighbor]:
                    tentative_distances[neighbor] = new_tentative_distance
                    heappush(nodes_to_visit, (new_tentative_distance, neighbor))
            
            seen.add(node)

        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)