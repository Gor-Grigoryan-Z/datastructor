class Node:
    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def addNeighbour(self, node):
        if not isinstance(node, Node):
            node = Node(node)

        if node not in self.neighbours:
            self.neighbours.append(node)

class Graph:
    def __init__(self):
        self.nodes = {}

    def getPaths(self, start, end,path=[]):
        path = path+[start]
        if start == end:
            return [path]

        if start not in self.nodes:
            return []

        paths = []
        for node in self.nodes[start].neighbours:
            if not node.value in path:
                allPaths = self.getPaths(node.value, end, path)
                for p in allPaths:
                    paths.append(p)
        return paths

    def addNode(self, node):
        if not isinstance(node, Node):
            node = Node(node)

        if node.value not in self.nodes:
            self.nodes[node.value] = node

    def addEdge(self, start, end):
        if start in self.nodes and end in self.nodes:
            for key, node in self.nodes.items():
                if key == start:
                    node.addNeighbour(self.nodes[end])
	

    def getShortestPath(self, start, end, path = []):
        path = path+[start]
        if start == end:
            return path

        if start not in self.nodes:
            return None

        shortestPath = None
        for node in self.nodes[start].neighbours:
            if node.value not in path:
                sp = self.getShortestPath(node.value, end, path)
                if shortestPath is None or len(shortestPath) > len(sp):
                    shortestPath = sp
        return shortestPath
    


	
       
   
    def __str__(self):
        output = ""
        for key, node in self.nodes.items():
            output+=("{0}: {1}\n".format(key, [n.value for n in node.neighbours]))
        return output
    


graph = Graph()
graph.addNode("USA")
graph.addNode("Germany")
graph.addNode("Russia")
graph.addNode("Georgia")
graph.addNode("Armenia")
print("Creating edges")
graph.addEdge("USA", "Germany")
graph.addEdge("USA", "Russia")
graph.addEdge("Germany", "Russia")
graph.addEdge("Germany", "Georgia")
graph.addEdge("Russia", "Georgia")
graph.addEdge("Georgia", "Armenia")
print(graph)
print(graph.getPaths("USA", "Georgia"))
print(graph.getShortestPath("USA", "Georgia"))