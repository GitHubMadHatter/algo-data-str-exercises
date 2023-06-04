from typing import Generic, TypeVar, List
T = TypeVar('T')
"""
Tree Node
----------

This node represents a node in a Tree
Each node contains a value, a pointer to its parent and a list of children
"""

class Node(Generic[T]):
    _value: int
    _parent: 'Node[T]'
    _children: List['Node[T]']
    _subtree_size: int
    """
    Node Class
    -init: Sets the basic information such as the value it holds and next element
    -get_value: retrieves value of node
    -set_value: sets value for node
    -get_parent: return parent of node
    -add_child: adds the child node to the list of children
    -get_children: returns the list of children
    -num_children: returns the number of children belonging to a node
    -is_internal: checks if node is non-leaf
    -is_external: checks if node is leaf
    -is_root: checks if node is root
    """

    def __init__(self, value: T, parent: 'Node[T]' = None) -> None:
        """
        The initialisation of the node sets the value held by the node
        as well as the element it is linked to.
        :param value: The value of the node.
        :param parent: parent of the node
        """
        self._value = value
        self._parent = None
        self._children = []
        self._subtree_size = 1

    def get_value(self) -> T:
        """
        Getter method for the value of the node
        :return: The value of the node.
        """
        return self._value

    def set_value(self, value: T) -> None:
        """
        Setter method for the value of the node
        :param value: The value to set the node to.
        """
        self._value = value

    def get_parent(self) -> 'Node[T]':
        """
        Returns the parent of the node.
        :return: Node which is the parent of the given node
        """
        return self._parent
    
    def get_subtree_size(self) -> int:
        """
        Return subtree size of node
        :return: Integer that is the node's subtree size
        """
        return self._subtree_size

        
    def set_subtree_size(self, value: int) -> None:
        """
        :param value: Set subtree size to value
        """
        self._subtree_size = value
    
    def update_subtree_size(self, extra: int) -> None:
        self._subtree_size += extra
    
    def add_child(self, child: 'Node[T]') -> None:
        """
        Adds child to the children list of the 
        current node.
        """
        if (child != None):
            self._children.append(child)
            self._subtree_size += 1
    
    def get_children(self) -> List['Node[T]']:
        """
        Returns the children of the node.
        :return: The list of children belonging to the
        current node.
        """
        return self._children
    
    def num_children(self) -> int:
        """
        :return: The number of direct children
        belonging to the current node.
        """
        return len(self._children)

    def is_internal(p: 'Node[T]') -> bool:
        """
        Returns True if node is internal and false otherwise
        :param p: The given node
        """
        return p.num_children() > 0
        
    def is_external(p: 'Node[T]') -> bool:
        """
        Returns True if node is external and false otherwise
        :param p: The given node
        """
        return p.num_children() == 0
    
    def is_root(p: 'Node[T]') -> bool:
        """
        Returns True if node is root and false otherwise
        :param p: The given node
        """
        return p._parent == None
