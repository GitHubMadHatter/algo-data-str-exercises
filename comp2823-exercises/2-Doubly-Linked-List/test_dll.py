import unittest
# from itertools import chain to get list from iterable
# from typing import ... for type hinting

from Node import Node
from DoublyLinkedList import DoublyLinkedList

"""
Test cases for the Doubly Linked List problem.
"""

# DEFINE HELPERS HERE

class NodeTestCases(unittest.TestCase):
    """
    Test cases for the Node class.
    """

    node1 : Node
    node2 : Node
    node2 : Node

    def setUp(self) -> None:
        """
        Run before every test case
        c.f. tearDown() after each e.g. for deleting files created in tests
        c.f. setUpClass() and tearDownClass(), run once before/after all cases
        """

        self.node1 = Node(10, None, None)
        self.node2 = Node(["Hello"], None, None)
        self.node3 = Node([1, 2, 4], None, self.node2)
    
    def test_instantiate(self) -> None:
        """
        Testing init and getters
        """
        self.assertEqual(self.node1.get_value(), 10, "Checking value")
        self.assertEqual(self.node2.get_value(), ["Hello"], "Checking value")
        self.assertEqual(self.node3.get_value(), [1, 2, 4], "Checking value")

        self.assertEqual(self.node1.get_next(), None, "Checking next")
        self.assertEqual(self.node2.get_next(), None, "Checking next")
        self.assertEqual(self.node3.get_next(), None, "Checking next")

        self.assertEqual(self.node1.get_prev(), None, "Checking prev")
        self.assertEqual(self.node2.get_prev(), None, "Checking prev")
        self.assertEqual(self.node3.get_prev(), self.node2, "Checking prev")

    def test_setters(self) -> None:
        """
        Testing setter functions
        """
        # changing values
        self.node1.set_value(["Greetings"])
        self.node3.set_value(["Bye Bye"])
        self.assertEqual(self.node1.get_value(), ["Greetings"], "Checking set value")
        self.assertEqual(self.node3.get_value(), ["Bye Bye"], "Checking set value")

        # previous of node 1 already null
        self.node1.set_next(self.node2)
        self.node2.set_prev(self.node1)
        self.node2.set_next(self.node3)
        # previous and next of node 3 already set

        # testing current prev + next + values
        self.assertEqual(self.node1.get_prev(), None, "Checking set prev")
        self.assertEqual(self.node1.get_next(), self.node2, "Checking set next")
        self.assertEqual(self.node2.get_prev().get_value(), ["Greetings"], "Checking set prev")
        self.assertEqual(self.node2.get_next().get_value(), ["Bye Bye"], "Checking set next")
        self.assertEqual(self.node3.get_prev(), self.node2, "Checking set prev")
        self.assertEqual(self.node3.get_next(), None, "Checking set next")


class DLLTestCases(unittest.TestCase):
    """
    Test cases for the Doubly Linked List class.
    """

    def test_instantiate(self) -> None:
        """
        Testing initex
        """
        #node1 = Node()
        #self.assertEqual(type(node1), Node)

# Allows test execution by running test file alone
if __name__ == '__main__':
    unittest.main()