from node import Node
from typing import Generic, TypeVar, List

T = TypeVar('T')
"""
Tree
------

This is the tree file which is the main data structure for this lesson. The tree
contains a root node and each node can have an arbitrary number of children.

Your task is to implement the basic functions below.
"""

class Tree(Generic[T]):
    _size: int
    _root: Node[T]
    """
    Tree Class
    Holds nodes, which can have an arbitrary number of children, unless it is a
    leaf node, then it has 0 children.
    
    Each node in Tree is type <class Node> defined in 'node.py'
    -init: sets up tree with specified root node
    -get_size: get the size of the tree
    -is_empty: check if tree is empty
    -is_root: check if node is root
    -is_leaf: check if node is leaf
    -add_node: add given node as a child of specified parent
    -remove_node: remove node and the subtree rooted at that node from the tree
    -preorder: preorder traversal of tree
    -postorder: postorder traversal of tree

    """

    def __init__(self, root: 'Node[T]') -> None:
        """
        Initialise the Tree
        :param root: Root node of the tree
        """
        self._root = root
        self._size = 1 if (root != None) else 0

    def get_root(self) -> 'Node[T]':
        """
        :return: root node of tree
        """
        return self._root

    def get_size(self) -> int:
        """
        Return the size of the tree (number of nodes)
        """
        return self._size
    
    def is_empty(self) -> bool:
        """
        Return a boolean stating whether the tree is empty or not
        """
        return self._size == 0
        
    def is_root(self, p: 'Node[T]') -> bool:
        """
        Check whether the given node p is the root node
        :param p: node to be checked
        """
        return p.is_root()

    def is_leaf(self, p: 'Node[T]') -> bool:
        """
        Check whether the given node p is a leaf node
        :param p: node to be checked
        """
        return p.is_external()

    def add_node(self, p: 'Node[T]', parent: 'Node[T]') -> None:
        """
        Add child node to a node in the tree
        Increase the size of the tree by 1 here as well
        :param p: node to be added
        :param parent: parent of the node to be added
        """
        if (parent == None or p == None):
            return
        parent.add_child(p)
        p._parent = parent
        self._size += 1
        return

    def remove_node(self, p: 'Node[T]') -> None:
        """
        Remove the entire subtree rooted at the given node from the tree
        If p is the root node, set the tree's root to be None
        Make sure each node's subtree size is appropriately updated
        :param p: Node to be removed from tree
        """
        self._size -= (1 + p.get_subtree_size())
        if (p.is_root()):
            #p.set_subtree_size(1)
            #p._children = []
            self._root = None
        else:
            old_parent = p.get_parent()
            old_parent._children.remove(p)
            while old_parent != None:
                old_parent.update_subtree_size(-p.get_subtree_size())
                old_parent = old_parent.get_parent()
            p._parent = None

    def preorder(self, p: 'Node[T]', ls: List['Node[T]']) -> None:
        """
        Preorder traversal of the tree
        :param p: the node to visit
        :param ls: Add nodes in preorder fashion to this supplied list
        Note: Add a newly visited node to the END of the supplied list
        """
        ls.append(p)

        if p.is_external():
            return
        for child in p.get_children():
            self.preorder(child, ls)
        
    
    def postorder(self, p: 'Node[T]', ls: List['Node[T]']) -> None:
        """
        Postorder traversal of the tree
        :param p: the node to visit
        :param ls: Add nodes in postorder fashion to this supplied list
        Note: Add a newly visited node to the END of the supplied list 
        """
        if p.is_external():
            ls.append(p)
            return
        for child in p.get_children():
            self.postorder(child, ls)
        ls.append(p)

