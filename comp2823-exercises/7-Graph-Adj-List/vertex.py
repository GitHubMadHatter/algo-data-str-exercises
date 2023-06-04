"""
Vertex 
-------

Given the current implementation an Adjacency list structure, each vertex
will only store ONE associated element. 

It supports the operation to get the stored element. 

"""

from typing import TypeVar, Generic, List

T = TypeVar('T')

class Vertex(Generic[T]):
    _element: T
    _edges: List['Edge[T]']

    def __init__(self, element: T) -> None:
        """
        Initialises a Vertex object.
        :param element: Element to be stored in Vertex object. 
        """
        
        self._element = element
        self._edges = []

    def get_element(self) -> T:
        """
        Returns the associated object stored within the vertex.
        :return: Return the element stored within the vertex.
        """
        return self._element
    
    def get_incident_edges_list(self) -> List['Edge[T]']:
        """
        Returns vertex object v.
        :return: Vertex object representing vertex v.
        """
        
        return self._edges

    def insert_edge(self, e: 'Edge[T]') -> None:
        """
        Adds edge into list of incident edges
        """
        self._edges.append(e)
        
