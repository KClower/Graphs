"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}


    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Initialize the vertex with an empty set of edges
        self.vertices[vertex_id] = set()
        return self.vertices[vertex_id]


    def add_edge(self, v1, v2):
        """
        Add a directed edge from v1 to v2 in the graph.
        """
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        # Add v2 to the adjacency set of v1
        self.vertices[v1].add(v2)
        

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Initialize a queue and add the starting vertex
        queue = deque([starting_vertex])
        # Creater a set to keep track of the visited vertices
        visited = set()

        while queue:
            # Dequeue a vertex form the front of the queue
            current_vertex = queue.popleft()

            # If we have't visited this vertex yet print the vertex (or process it in some way)
            if current_vertex not in visited:
                print(current_vertex)
                # Mark it as visited
                visited.add(current_vertex)

                # Add all unvisited neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited:
                        queue.append(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Initialize a stack with the starting vertex
        stack = [starting_vertex]
        # Create a set to keep track  of the visited vertices
        visited = set()

        while stack:
            # Pop a vertex from the top of the stack
            current_vertex = stack.pop()

            # If we haven't visited this vertex yet
            if current_vertex not in visited:
                # Print the vertex (or process it in some way)
                print(current_vertex)
                # Mark it as visited
                visited.add(current_vertex)

                # Add all unvisited neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited:
                        stack.append(neighbor)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Initialize the visited set only once
        if visited is None:
            visited = set()

        # Print the current vertex
        print(starting_vertex)
        # Mark it as visited
        visited.add(starting_vertex)

        # Reclusively visit each unvisited neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Initialize the queue with the starting path
        queue = deque([[starting_vertex]])
        # Create set to keep track of visited vertices
        visited = set()

        while queue:
            # Dequeue the current path
            path = queue.popleft()
            # Get the last vertex in the path
            current_vertex = path[-1]

            # If we found the destination, return the path
            if current_vertex == destination_vertex:
                return path
            
            # If the current path has not been visited 
            if current_vertex not in visited:
                # Mark it as visited
                visited.add(current_vertex)

                # Enqueue paths to each neighbor
                for neighbor in self.get_neighbors(current_vertex):
                    # Copy the current path and append the neighbor
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        # Return None if no path is found
        return None
    

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Initialize a stack with the starting path
        stack = [[starting_vertex]]
        # Create a set to keep track of the visited vertices
        visited = set()

        while stack:
            # Pop the current path from the stack
            path = stack.pop()
            # Get the last vertex in the path
            current_vertex = path[-1]

            # If we found the destination, return the path
            if current_vertex == destination_vertex:
                return path
            
            # If the current vertex has not been visited
            if current_vertex not in visited:
                # Mark as visited
                visited.add(current_vertex)

            # Push paths to each neighbor onto the stack
            for neighbor in self.get_neighbors(current_vertex):
                # Create a new path including the neighbor
                new_path = list(path) # Make a copy of the current path
                new_path.append(neighbor)
                stack.append(new_path)

        # Return None if no path is found
        return None
    

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Initialize path and visited set only on the first call
        if path is None:
            path = []
        if visited is None:
            visited = set()

        # Add the starting vertex to the path and mark it as visited
        path.append(starting_vertex)
        visited.add(starting_vertex)

        # If we found the destination, return the current path
        if starting_vertex == destination_vertex:
            return path
        
        # Recur for each neighbor that has not been visited
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                # Recursively call dfs_recursive for the neighbor
                result = self.dfs_recursive(neighbor, destination_vertex, list(path), visited)
                # If a path is found, return it
                if result is not None:
                    return result
                
        # If no path is found, return None
        return None
    


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/BloomInstituteOfTechnology/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
