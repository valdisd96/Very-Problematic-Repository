import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))

    def dijkstra(self, start):
        queue = []
        heapq.heappush(queue, (0, start))
        distances = {node: float('infinity') for node in self.edges}
        distances[start] = 0
        visited = set()

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, weight in self.edges.get(current_node, []):
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return distances

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 1)

    start_node = 'A'
    distances = graph.dijkstra(start_node)
    print(f"Distances from {start_node}: {distances}")