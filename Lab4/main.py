class OrientedGraph():
    def __init__(self, edges: list[tuple[str, str, int]]):
        self.edges = edges
        self.edges.sort()
        self.vertexes = []
        self.vertexes.extend([edge[0] for edge in edges])
        self.vertexes.extend([edge[1] for edge in edges])
        self.vertexes.sort()
        self.vertexes = set(self.vertexes)
        self.source = min(self.vertexes)
        self.target = max(self.vertexes)
        self.topological_order = self.topological_sort()

    def topological_sort(self):
        visited = dict.fromkeys(self.vertexes, False)
        sorted = []

        def travel_from_vertex(vertex: str):
            visited[vertex] = True
            for edge in self.edges:
                if edge[0] == vertex and not visited[edge[1]]:
                    travel_from_vertex(edge[1])

            sorted.append(vertex)    

        for vertex in self.vertexes:
            if not visited[vertex]:
                travel_from_vertex(vertex)
        
        sorted.reverse()
        return sorted

    def max_length_path(self):
        OPT = dict.fromkeys(self.vertexes, -float("inf"))
        x = dict.fromkeys(self.vertexes)
        
        OPT[self.source] = 0

        for vertex in self.topological_order:
            if vertex == self.target:
                break
            for edge in [edge for edge in self.edges if edge[0] == vertex]:
                new_opt = OPT[edge[0]] + edge[2]
                if new_opt > OPT[edge[1]]:
                    OPT[edge[1]] = new_opt
                    x[edge[1]] = edge[0]

        if OPT[self.target] == -float("inf"):
            return None, None

        path = []
        current_vertex = self.target
        while current_vertex != None:
            path.append(current_vertex)
            current_vertex = x[current_vertex]
        path.reverse()

        return path, OPT[self.target]

def main():
    # E = [
    #     ("a", "c", 5),
    #     ("a", "b", 4),
    #     ("c", "b", 2),
    #     ("b", "d", 3)
    # ]

    # E = [
    #     ("a", "c", 5),
    #     ("a", "b", 4),
    #     ("c", "b", 2),
    #     ("b", "d", 3),
    #     ("e", "f", 3),
    # ]

    E = [
        ("a", "e", 5),
        ("a", "b", 4),
        ("e", "b", 2),
        ("b", "f", 3),
        ("c", "d", 3),
    ]

    G = OrientedGraph(E)
    path, OPT = G.max_length_path()
    if path is None:
        print("Can't reach the target from source")
    else:
        print(f"The path with max length {OPT}, from source to target:\n{path}")


if __name__ == "__main__":
    main()