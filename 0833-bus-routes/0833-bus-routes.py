from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        # graph = defaultdict(list)
        # for stops in routes:
        #     for i in range(len(stops)):
        #         graph[route[i-1]].append(route[i])
        #         graph[route[i]].append(route[i-1])
        if source == target:
            return 0

        n = len(routes)

        # To check if there are stops in common
        routes_sets = [set(route) for route in routes]

        # Graph with routes as nodes and edges between routes that have stops in common
        routes_graph = defaultdict(list)

        # BFS
        queue = deque()
        seen = set()

        # Create graph of routes
        # Loop on every route
        for route in range(n):
            # And every other route
            for other_route in range(route+1, n):
                # If they have a stop in common, add edges between there nodes
                if routes_sets[route].intersection(routes_sets[other_route]):
                    routes_graph[route].append(other_route)
                    routes_graph[other_route].append(route)
            
            # If source is on this route
            if source in routes_sets[route]:
                # If target is also on this route, return 1
                if target in routes_sets[route]:
                    return 1
                # Else, add it to the BFS queue
                queue.append((1, route))
                seen.add(route)

        while queue:
            path_length, route = queue.popleft()
            
            for connected_route in routes_graph[route]:
                if target in routes_sets[connected_route]:
                    return path_length + 1
                if connected_route not in seen:
                    queue.append((path_length + 1, connected_route))
                    seen.add(route)
            
        return -1
