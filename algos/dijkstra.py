from collections import defaultdict, deque


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        for i in range(0,31):
            for j in range(51):
                self.add_node(str(i)+'-'+str(j))

        for i in range(30):
            for j in range(50):
                self.add_edge(str(i)+'-'+str(j),str(i)+'-'+str(j+1))
                self.add_edge(str(i)+'-'+str(j+1),str(i)+'-'+str(j))
                self.add_edge(str(i)+'-'+str(j),str(i+1)+'-'+str(j))
                self.add_edge(str(i+1)+'-'+str(j),str(i)+'-'+str(j))

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance=1):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial, destination):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge == destination:
                visited[edge] = weight
                path[edge] = min_node
                break
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
        if min_node == destination:
            break

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin, destination)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited, list(full_path)


    