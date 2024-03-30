# importing Libraries
import heapq

# defining class "Graph"
class Graph:
    def __init__(self, graph):
        self.graph = {node.upper(): {k.upper(): v for k, v in edges.items()} for node, edges in graph.items()}

    # implementing dijkstra algorithm
    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

    # finding shortest path to charging station
    def shortest_paths_to_charging_stations(self, start, charging_stations):
        shortest_paths = {}
        distance = self.dijkstra(start)

        for station in charging_stations:
            shortest_paths[station] = distance.get(station.upper(), float('inf'))

        return shortest_paths
    # recommending route for shortest path
    def recommend_route(self, start, charging_stations):
        shortest_paths = self.shortest_paths_to_charging_stations(start, charging_stations)
        recommended_station = min(shortest_paths, key=shortest_paths.get)
        return recommended_station.upper()

# constructing the graph
graph = {
    'A': {'B': 6, 'F': 5},
    'B': {'A': 6, 'C': 5, 'G': 6},
    'C': {'B': 5, 'D': 7, 'H': 5},
    'D': {'C': 7, 'E': 7, 'I': 8},
    'E': {'D': 7, 'I': 6, 'N': 15},
    'F': {'A': 5, 'G': 8, 'J': 7},
    'G': {'B': 5, 'F': 8, 'H': 9, 'K': 8},
    'H': {'G': 9, 'C': 5, 'I': 12},
    'I': {'H': 12, 'D': 8, 'E': 6, 'M': 10},
    'J': {'F': 7, 'K': 5, 'O': 7},
    'K': {'J': 5, 'G': 8, 'L': 7},
    'L': {'K': 7, 'P': 7, 'M': 7},
    'M': {'L': 7, 'I': 10, 'N': 9},
    'N': {'M': 9, 'E': 15, 'R': 7},
    'O': {'J': 7, 'P': 13, 'S': 9},
    'P': {'O': 13, 'Q': 8, 'L': 7, 'U': 11},
    'Q': {'P': 8, 'R': 9},
    'R': {'Q': 9, 'N': 7, 'W': 10},
    'S': {'O': 9, 'T': 9},
    'T': {'S': 9, 'U': 8},
    'U': {'T': 8, 'P': 11, 'V': 8},
    'V': {'U': 8, 'W': 5},
    'W': {'V': 5, 'R': 10}
}

# creating Graph instance
graph = Graph(graph)

# charging stations
charging_stations = {'H', 'K', 'Q', 'T'}

# asking for the starting node
start_node = input("Enter the starting node: ").upper()

# checking if starting node is a charging station
if start_node in charging_stations:
    print("You are already at a charging station.")
else:
    # finding the shortest paths to charging stations
    shortest_paths = graph.shortest_paths_to_charging_stations(start_node, charging_stations)
    print("Shortest paths to charging stations from node", start_node + ":")
    for station, distance in shortest_paths.items():
        print(f"To station {station}: Distance = {distance}")

    # recommending the most efficient route
    recommended_station = graph.recommend_route(start_node, charging_stations)
    print("\nRecommended charging station based on shortest distance:", recommended_station)
