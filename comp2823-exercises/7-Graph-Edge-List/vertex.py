"""
Vertex 
-------

Given the current implementation an Edge list structure, each vertex
will only store ONE associated element. 

It supports the operation to get the stored element. 

"""

from typing import TypeVar, Generic

T = TypeVar('T')

class Vertex(Generic[T]):
    _element: T

    def __init__(self, element: T) -> None:
        """
        Initialises a Vertex object.
        :param element: Element to be stored in Vertex object. 
        """
        
        self._element = element

    def get_element(self) -> T:
        """
        Returns the associated object stored within the vertex.
        :return: Return the element stored within the vertex.
        """
        return self._element
