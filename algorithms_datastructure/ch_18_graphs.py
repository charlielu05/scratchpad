from typing import List


# Vertex class for directed Graphs
class Vertex:
    def __init__(self, value:str):
        self.value = value
        self.adjacent_vertex:Vertex = []
    
    def __repr__(self):
        return self.value
    
    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertex.append(vertex)
        
class UndirectedVertex(Vertex):
    # for undirected graph relationship
    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertex.append(vertex)
        
        if self in vertex.adjacent_vertex:
            return None
        else:
            vertex.add_adjacent_vertex(self)

# depth first traverse
def dfs_traverse(vertex:Vertex, visited_vertices={}):
    visited_vertices[vertex.value] = True
    
    print(vertex.value)
    
    # iterate through the current vertex's adjacent vertices
    for vertex_node in vertex.adjacent_vertex:
        # ignore the vertex node if already visited
        if visited_vertices.get(vertex_node.value):
            continue
        else:
            dfs_traverse(vertex_node, visited_vertices)

# depth first traverse search
def dfs_traverse_search(vertex:Vertex, search_value:str, visited_vertices={}):
    visited_vertices[vertex.value] = True
    
    # return the vertex if it is the search_value
    if vertex.value == search_value:
        return vertex
    
    # iterate through the current vertex's adjacent vertices
    for vertex_node in vertex.adjacent_vertex:
        # return vertex_node if it is the search value
        if vertex_node.value == search_value:
            return vertex_node
        else:
            # ignore the vertex node if already visited
            if visited_vertices.get(vertex_node.value):
                continue
            else:
                vertex_searching_for = dfs_traverse_search(vertex_node, search_value, visited_vertices) 
                
    return vertex_searching_for if "vertex_searching_for" in locals() else None

def bfs_search(vertex:Vertex, search_value:str, visited_vertices={}):

    def bfs_loop(current_vertex:Vertex):
        for vertex in current_vertex.adjacent_vertex:
          
            if visited_vertices.get(vertex.value):
                continue
            else: 
                print(vertex.value)
                visited_vertices[vertex.value] = True
                bfs_queue.append(vertex)
        
    # start at any vertex, this is the starting vertex
    # add the starting vertex to hash table to indicate visited
    visited_vertices[vertex.value] = True
    
    # add the starting vertex to a queue
    # we use python list and only take the start
    bfs_queue = []
    bfs_queue.append(vertex)
    
    # start loop that runs while queue is not empty
    while len(bfs_queue) != 0:
        # remove first vertex from the queue, call it current vertex
        current_vertex:Vertex = bfs_queue.pop(0)
        bfs_loop(current_vertex)
        
    
if __name__ ==  "__main__":
    alice = Vertex("alice")
    bob = Vertex("bob")
    cynthia = Vertex("cynthia")
    
    alice.add_adjacent_vertex(bob)
    alice.add_adjacent_vertex(cynthia)
    bob.add_adjacent_vertex(cynthia)
    cynthia.add_adjacent_vertex(bob)
    
    # undirected graphs
    kim = UndirectedVertex("kim")
    charlie = UndirectedVertex("charlie")
    charlotte = UndirectedVertex("charlotte")
    
    kim.add_adjacent_vertex(charlie)
    
    assert kim in charlie.adjacent_vertex
    
    # depth first search
    dfs_traverse(alice)
    dfs_traverse(kim)
    
    # breadth first search
    alice = UndirectedVertex("alice")
    bob = UndirectedVertex("bob")
    candy = UndirectedVertex("candy")
    derek = UndirectedVertex("derek")
    elaine = UndirectedVertex("elaine")
    fred = UndirectedVertex("fred")
    gina = UndirectedVertex("gina")
    helen = UndirectedVertex("helen")
    irena = UndirectedVertex("irena")
    
    # create the relationships
    alice.add_adjacent_vertex(bob)
    alice.add_adjacent_vertex(candy)
    alice.add_adjacent_vertex(derek)
    alice.add_adjacent_vertex(elaine)
    
    bob.add_adjacent_vertex(fred)
    fred.add_adjacent_vertex(helen)
    candy.add_adjacent_vertex(helen)
    derek.add_adjacent_vertex(elaine)
    derek.add_adjacent_vertex(gina)
    gina.add_adjacent_vertex(irena)    

    print("BFS")
    bfs_search(alice, '0')
    