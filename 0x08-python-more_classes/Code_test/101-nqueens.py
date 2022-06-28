#!/usr/bin/python3
"""
    101-nqueens Module
"""
from sys import argv, exit


class Solution:
    """
        solution class
    """

    def solve(self, n):
        """
            solves the nqueen problem

            Args:
                n: size of chess board

            Return:
                list of positions
        """
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions

    def is_valid_state(self, state, n):
        """
            checks if it's a valid solution

            Args:
                state: positions queen occupies

            Returns
                True if a valid solution else False
        """
        return len(state) == n

    def get_candidates(self, state, n):
        """
            gets the indexes of the position the queen can occupy

            Args:
                state: position queen occupies
                n: size of the chessboard

            Returns:
                the indexes of the position the queen can occupy
        """
        if not state:  # no queen is on the board
            return range(n)

        # find the next position to place queen
        position = len(state)
        candidates = set(range(n))
        # remove indexes/camdidates that place queen into attacks

        for row, col in enumerate(state):
            # discard col index if it's occupied
            candidates.discard(col)
            distance = position - row
            #  discard diagonals
            candidates.discard(col + distance)  # diagonal right
            candidates.discard(col - distance)  # diagonal left
        return candidates

    def search(self, state, solutions, n):
        """
            searches if the queen can stay at an candidate index
            without being attacked by another queen

            Args:
                state: position queen occupies
                solutions: 2D list containing positions queen can stay
                n: size of chessboard
        """

        if self.is_valid_state(state, n):
            state_list = self.state_to_list(state)
            solutions.append(state_list)
            return

        for candidate in self.get_candidates(state, n):
            # recurse till valid state is found
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()  # restore modified state back to original

    def state_to_list(self, state):
        """
            converts state indexes to coordinate list

            Args:
                state: position queen occupies

            Returns:
                list of coordinates the queen occupies without attacking
                each other
        """
        res = []
        for row, col in enumerate(state):
            coordinate = []
            coordinate.append(row)
            coordinate.append(col)
            res.append(coordinate)
        return res


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    solution = Solution()
    list_of_sol = solution.solve(N)

    for res in list_of_sol:
        print(res)
