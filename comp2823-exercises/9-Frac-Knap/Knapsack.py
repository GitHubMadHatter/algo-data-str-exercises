from typing import List, Tuple

"""
KnapSack
----------

This class will represent your Knapsack.
There is one function to implement: `fractional_knapsack` which will be called with the relevant set of items
along with a corresponding capacity. It should return the maximum possible value that can be obtained.

You are guaranteed the following bounds:
 - 0 <= capacity <= 1000000
 - 0 <= len(items) <= 100000
For each item i:
 - 1 <= w_i <= 1000000
 - 0 <= v_i <= 1000000

All inputs are also guaranteed to be integers (no floats).
Your solution will be classified as correct if it is within +- 1E-5 of the correct answer.
"""


class KnapSack:

    def __init__(self):
        pass

    def fractional_knapsack(self, items: List[Tuple[int, int]], capacity: int) -> float:
        """
        This function will solve the knapsack problem using the fractional knapsack algorithm.
        Recall that the fractional knapsack problem allows you to take fractional amounts of items.
        :param items: A list of tuples containing the weight and value of each item respectively.
        :param capacity: The capacity of the knapsack.
        :return: The maximum value that can be obtained into the knapsack.
        """

        # TODO: Implement this function.
        return 0.0

