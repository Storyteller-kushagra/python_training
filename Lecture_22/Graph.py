class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbours = []


def __repr__(self):
    return str(self.value)


class Graph:
    def __init__(self):
        self.vertices = []

    def find(self, value):
        for vertex in self.vertices:
            if vertex.value == value:
                return vertex
            return None

    def add_vertex(self, value):
        if not self.find(value):
            self.vertices.append(Vertex(value))
        else:
            print(value, "already exist")

    def add_edge(self, source, target):
        source_v = self.find(source)
        target_v = self.find(target)

        if source_v and target_v:
            source_v.neighbours.append(target_v)
            target_v.neighbours.append(source_v)

        else:
            print("Some of", source, target, "are missing")

    def display(self):
        for vertex in self.vertices:
            print(vertex, ":" , vertex.neighbours)

    def depth_first_trav(self, source = None):
        if not source:
            vertex = self.vertices[0]
        else:
            vertex = self.find(source)

        stack = list()
        visited = set()

        stack.append(vertex)
        visited.append(vertex)

        while len(stack) > 0:
            vertex = stack.pop()
            print(vertex)

            for neighbour in vertex.neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

    def depth_first_search(self):
        if not source:
            vertex = self.vertices[0]
        else:
            vertex = self.find(source)

        stack = list()
        visited = set()

        stack.append(vertex)
        visited.append(vertex)

        while len(stack) > 0:
            vertex = stack.pop()
            print(vertex)

            for neighbour in vertex.neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)


if __name__ == "__main__":

    graph = Graph()
    graph.add_vertex("Ravi")
    graph.add_vertex("Rahul")
    graph.add_edge("Ravi", "Rahul")

    graph.depth_first_trav()