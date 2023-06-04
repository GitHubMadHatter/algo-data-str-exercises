"""
UNDIRECTED Graph ADT

Edge List Structure 
-------

"""

from typing import TypeVar, Generic, List
from vertex import Vertex
from edge import Edge

T = TypeVar('T')

class Graph(Generic[T]):
    _vertices: List[Vertex[T]]
    _edges = List[Edge[T]]

    """
    Undirected Graph class 
    Holds a list of vertices and a list of edges. 

    Each vertex in the graph is type <class Vertex> defined in 'vertex.py'.

    Init: Sets up a graph with no vertices and no edges. 

    Recall: Given our Edge List Structure, each edge object points to the 
    2 vertices it connects, but the vertices do not point back to the edges.     
    
    """

    def __init__(self) -> None:
        self._vertices = []
        self._edges = [] 

    def num_vertices(self) -> int:
        """
        Returns the number of vertices in the graph.
        :return: The number of vertices in the graph.
        """

        # TODO implement me.

    def list_vertices(self) -> List[Vertex[T]]:
        """
        Returns a list of all the vertices of the graph.
        :return: The list of all the vertex objects in the graph.
        """

        # TODO implement me.

    def num_edges(self) -> int:
        """
        Returns the number of edges of the graph. 
        :return: The number of edges in the graph.
        """

        # TODO implement me.

    def list_edges(self) -> List[Edge[T]]:
        """
        Returns a list of all the edges of the graph. 
        :return: The list of all the edge objects in the graph.
        """

        # TODO implement me.

    def get_edge(self, u: Vertex[T], v: Vertex[T]) -> Edge[T]:
        """
        Returns the edge from vertex u to vertex v, if one exists; 
        Otherwise return None (including when u or v is None) 
        :param u: The vertex object representing vertex u.
        :param v: The vertex object representing vertex v.
        :return: The edge object representing the edge connecting vertices u and v.
        """
        
        # TODO implement me.


    def end_vertices(self, e: Edge[T]) -> List[Vertex[T]]:
        """
        Returns an array containing the two endpoint vertices of edge e.
        Return None if edge e is None.  
        :param e: The edge object representing edge e.
        :return: The list containing vertex objects which represent the two endpoint vertices of edge e.
        """

        # TODO implement me.


    def opposite(self, v: Vertex[T], e: Edge[T]) -> Vertex[T]:
        """
        For edge e incident to vertex v, returns the other vertex of the edge; 
        Return None if e is not incident to v, or if either v or e is None. 
        :param v: The vertex object representing vertex v.
        :param e: The edge object representing edge e.
        :return: The vertex object that represents the other vertex endpoint of edge e.
        """

        # TODO implement me.


    def degree(self, v: Vertex[T]) -> int:
        """
        Returns the number of edges incident to vertex v. 
        Return None if v is None.  
        :param v: The vertex object representing vertex v.
        :return: The integer representing the number of edges incident to v.
        """

        # TODO implement me.

    def incident_edges(self, v: Vertex[T]) -> List[Edge[T]]:
        """
        Returns a list of all edges incident to vertex v. 
        Return None if v is None.
        :param v: The vertex object representing vertex v.
        :return: The list of edge objects representing all the edges incident to vertex v.
        """

        # TODO implement me.


    def insert_vertex(self, x: T) -> Vertex[T]:
        """
        Creates and returns a new Vertex storing element x. 
        :param x: The element associated with the newly created vertex object.
        :return: The newly created vertex object.
        """

        # TODO implement me.


    def insert_edge(self, u: Vertex[T], v: Vertex[T], x: T) -> Edge[T]:
        """
        Creates and returns a new Edge from vertex u to vertex v, 
        storing element x; return None if there already exists an 
        edge from u to v, or if either u or v are not already in the graph. 
        Also, return None if either u or v is None.
        :param u: The vertex object representing vertex u.
        :param v: The vertex object representing vertex v.
        :return: The edge object representing the newly created edge.
        """

        # TODO implement me.


    def remove_vertex(self, v: Vertex[T]) -> None:
        """
        Removes vertex v and all its incident edges from the graph. 
        Nothing happens if there does not exist a vertex v.
        Return None if v is None.
        :param v: Vertex to be removed. 
        """

        # TODO implement me.


    def remove_edge(self, e: Edge[T]) -> None: 
        """
        Removes edge e from the graph. 
        Nothing occurs if there does not exist an edge e. 
        Return None if e is None.
        :param e: Edge to be removed. 
        """

        # TODO implement me.

