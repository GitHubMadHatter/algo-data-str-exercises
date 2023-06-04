"""
Edge 
-------

For each undirected edge e that connects vertices u and v, e will store:
- One associated element 
- u <Vertex class>
- v <Vertex class>

It supports the operation to get the stored element, as well 
as getter methods for u and v. 


"""

from typing import TypeVar, Generic

T = TypeVar('T')

class Edge(Generic[T]):
    _element: T
    _u: 'Vertex[T]'
    _v: 'Vertex[T]'

    def __init__(self, element: T, u: 'Vertex[T]' = None, v: 'Vertex[T]' = None) -> None:
        """
        Initialises an undirected edge between vertex u and vertex v,
        storing element.
        :param element: The element to be stored at the edge.
        :param u: The vertex object representing vertex u.
        :param v: The vertex object representing vertex v.
        """
        self._element = element
        self._u = u
        self._v = v

    def get_element(self) -> T:
        """
        Returns the associated object stored within the edge.
        :return: Element stored within edge.
        """
        
        return self._element

    def get_vertex_u(self) -> 'Vertex[T]':
        """
        Returns vertex object u.
        :return: Vertex object representing vertex u.
        """
        
        return self._u
        
    def get_vertex_v(self) -> 'Vertex[T]':
        """
        Returns vertex object v.
        :return: Vertex object representing vertex v.
        """
        
        return self._v
