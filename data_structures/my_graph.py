from .time_logger import time_logger


class Graph:

    def __init__(self, directed=False):
        self.directed = directed
        self.adjacency_list = dict()

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return list(self.adjacency_list.keys())[0] == list(other.adjacency_list.keys())[0]
        else:
            return NotImplemented
        
    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result
        
    def __ge__(self, other):
        if self.__class__ == other.__class__:
            return list(self.adjacency_list.keys())[0] >= list(other.adjacency_list.keys())[0]
        else:
            return NotImplemented

    def __gt__(self, other):
        if self.__class__ == other.__class__:
            return list(self.adjacency_list.keys())[0] > list(other.adjacency_list.keys())[0]
        else:
            return NotImplemented

    def __le__(self, other):
        if self.__class__ == other.__class__:
            return list(self.adjacency_list.keys())[0] <= list(other.adjacency_list.keys())[0]
        else:
            return NotImplemented

    def __lt__(self, other):
        if self.__class__ == other.__class__:
            return list(self.adjacency_list.keys())[0] < list(other.adjacency_list.keys())[0]
        else:
            return NotImplemented

    def __repr__(self):
        graph = ""

        for node, neighbors in self.adjacency_list:
            graph += f"{node}: {neighbors}\n"

        return graph

    @time_logger
    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = set()
        else:
            raise ValueError("Node already exists.")

    @time_logger
    def remove_node(self, node):
        if node not in self.adjacency_list:
            raise ValueError("Node does not exists.")
        else:
            for neighbors in self.adjacency_list.values():
                neighbors.discard(node)

            del self.adjacency_list[node]

    @time_logger
    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adjacency_list:
            raise ValueError("Node does not exists.")
        
        if to_node not in self.adjacency_list:
            raise ValueError("Node does not exists.")
        
        if weight is None:
            self.adjacency_list[from_node].add(to_node)

            if not self.directed:
                self.adjacency_list[to_node].add(from_node)
        else:
            self.adjacency_list[from_node].add((to_node, weight))

            if not self.directed:
                self.adjacency_list[to_node].add((from_node, weight))

    @time_logger
    def remove_edge(self, from_node, to_node):
        if from_node in self.adjacency_list:
            if to_node in self.adjacency_list[from_node]:
                self.adjacency_list[from_node].remove(to_node)
            else:
                raise ValueError("Edge does not exists.")
        else:
            raise ValueError("Node does not exists.")

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, set())

    def has_node(self, node):
        return node in self.adjacency_list

    def has_edge(self,from_node, to_node):
        if from_node in self.adjacency_list:
            return to_node in self.adjacency_list[from_node]
        return False
    
    def get_nodes(self): 
        return list(self.adjacency_list.keys())
    
    def get_edges(self):
        return [(from_node, to_node) for from_node, neighbors in self.adjacency_list.items() for to_node in neighbors]

    def bfs(self, from_node):
        visited = set()
        queue = [from_node]
        order = []

        while queue:
            node = queue.pop(0)

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbors = self.get_neighbors(node)
                for neighbor in neighbors:
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    
                    if neighbor not in visited:
                        queue.append(neighbor)

        return order

    def dfs(self, from_node):
        visited = set()
        stack = [from_node]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbors = self.get_neighbors(node)
                for neighbor in sorted(neighbors, reverse=True):
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    
                    if neighbor not in visited:
                        stack.append(neighbor)

        return order
