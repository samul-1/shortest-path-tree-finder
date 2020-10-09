class Node:
    def __init__(self, number, label, is_root=False):
        self.number = number
        self.predecessor = None
        self.label = label
        self.is_root = is_root
        self.visited = -1
    def __str__(self): # for debugging purposes
        return str(self.number) + ", pred " + str(self.predecessor.number if self.predecessor != None else "None") + ", label " + str(self.label) + "\n"

class Edge:
    def __init__(self, source, dest, cost, is_tree_edge=False):
        self.source = int(source)
        self.dest = int(dest)
        self.cost = int(cost)
        self.is_tree_edge = is_tree_edge
    
    def get_edge_as_triple(self): # returns a triple (i, j, c) where i is the source of the edge, j the destination, and c the cost
        return (self.source, self.dest, self.cost)
        
    def get_edge_as_couple(self): # returns a couple (i, j) where i is the source of the edge, j the destination
        return (self.source, self.dest)


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
    
    def get_node_from_number(self, number): # returns the node that has matching number attribute
        for node in self.nodes:
            if number == node.number:
                return node
        return None

    def get_edge_from_nodes(self, i, j): # returns an edge (i, j) where i and j are the given nodes
        for edge in self.edges:
            if edge.source == i.number and edge.dest == j.number:
                return edge
        return None

    def get_all_edges_as_couples(self, only_tree=False): # returns a list of edges in the form (i, j)
        arr = []
        for edge in self.edges:
            if(not only_tree or only_tree and edge.is_tree_edge):
                arr.append(edge.get_edge_as_couple())
        return arr

    def get_all_node_numbers(self):
        for node in self.nodes:
            yield node.number
    
    def get_edge_costs(self, only_tree=False): # returns a dictionary edge_as_couple:cost
        dic = {}
        for edge in self.edges:
            if(not only_tree or only_tree and edge.is_tree_edge):
                dic[edge.get_edge_as_couple()] = edge.cost
        return dic
    
    def get_bn(self, node): # returns the backwards nodes list of given node
        bn = []
        for edge in self.edges:
            if edge.get_edge_as_triple()[1] == node:
                bn.append(edge.get_edge_as_triple())
        return bn
    
    def get_fn(self, node): # returns the forwards nodes list of given node
        fn = []
        for edge in self.edges:
            if edge.get_edge_as_triple()[0] == node.number:
                fn.append(edge)
        return fn

    def bfs(self, src): # breadth-first search traverse of the graph
        import queue
        q = queue.Queue()
        q.put(self.get_node_from_number(src))
        while not q.empty():
            v = q.get()
            fn = self.get_fn(v)
            for edge in fn:
                dest = self.get_node_from_number(edge.get_edge_as_triple()[1])
                cost = edge.get_edge_as_triple()[2]
                if dest.visited == -1:
                    dest.visited = 0
                    dest.predecessor = v
                    dest.label += v.label + cost
                    edge.is_tree_edge = True
                    q.put(dest)
            v.visited = 1
    
    def print_graph(self): # prints all nodes as stings
        for node in self.nodes:
            print(node)

    def print_tree_edges(self): # prints the list of edges that make up the tree from the graph
        for edge in self.edges:
            if(edge.is_tree_edge):
                print(edge.get_edge_as_triple())

    def is_spt(self): # returns True if the tree made up by tree edges is a shortest path tree, False otherwise
        for node in self.nodes:
            fn = self.get_fn(node)
            for edge in fn:
                if node.label + edge.cost < self.get_node_from_number(edge.dest).label:
                    return False
        return True
    
    def build_spt(self, root): # applies a Bellman Ford's-like algorithm to build an spt tree from the graph
        import queue

        q = []
        for node in self.nodes:
            q.append(node)

        while len(q):
            u = q.pop(0)
            fn = self.get_fn(u)
            for edge in fn:
                v = self.get_node_from_number(edge.dest)
                if u.label + edge.cost < v.label:
                    self.get_edge_from_nodes(v.predecessor, v).is_tree_edge = False
                    v.predecessor = u
                    v.label = u.label + edge.cost
                    if not v in list(q):
                        q.append(v)
                    edge.is_tree_edge = True
    
    def draw_graph(self, figure, source, only_tree=False): # draws a graph on the screen. if only_tree is True, only tree edges are drawn
        import networkx as nx
        import matplotlib.pyplot as plt

        # set things up for the graph to be drawn on screen
        G = nx.DiGraph()
        plt.figure(figure)
        G.add_edges_from(self.get_all_edges_as_couples(only_tree))
        pos = nx.shell_layout(G)
        nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size = 500)
        nx.draw_networkx_edges(G, pos, edge_color='r', arrows=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=self.get_edge_costs(only_tree), )
        nx.draw_networkx_labels(G, pos)
        plt.show()



def get_graph(): # builds a graph from user input and returns it
    number_of_nodes = input("Number of nodes: ")
    nodes = get_nodes(number_of_nodes)
    
    number_of_edges = input("Number of edges: ")
    edges = get_edges(number_of_edges)

    graph = Graph(nodes, edges)
    return graph

def get_nodes(n): # builds a list of n Nodes from user input and returns it
    nodes = []
    for i in range(0, int(n)):
        n = int(input())
        node = Node(n, 0)
        nodes.append(node)
    return nodes


def get_edges(n): # builds a list of n Edges from user input and returns it
    edges = []
    for i in range(0, int(n)):
        j = int(input())
        k = int(input())
        c = int(input())
        edge = Edge(j, k, c)
        edges.append(edge)
    return edges

# Driver code
import time
graph = get_graph()
graph.bfs(1)

print("Traversing the graph...")
graph.draw_graph(1, 1)

print("\nTree edges from BST: ")
graph.print_tree_edges()

time.sleep(1)

graph.draw_graph(2, 1, True)

if(graph.is_spt()): 
    print("This tree is an SPT") 
else: 
    print("This tree is not an SPT")
    graph.build_spt(1)
    print("Here's an SPT built from this graph:")
    graph.print_tree_edges()
    time.sleep(1)
    graph.draw_graph(3, 1, True)
