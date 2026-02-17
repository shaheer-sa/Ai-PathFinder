import matplotlib.pyplot as mat
import collections
import heapq

class AiPathfinder:
    def __init__(self):
        self.gridSize = 10
        self.grid = [[0 for _ in range(self.gridSize)] for _ in range(self.gridSize)]
        # Movement
        self.moveOrder = [
            (-1, 0),  # Up
            (0, 1),   # Right
            (1, 0),   # Bottom
            (1, 1),   # Bottom-Right
            (0, -1),  # Left
            (-1, -1)  # Top-Left
        ]

        self.start = (9, 4)
        self.target = (0, 6)
        
        # Walls
        for r in range(2, 6):
            self.grid[r][5] = -1

    # check valid movement
    def isValidMove(self, r, c):
        if 0 <= r < self.gridSize and 0 <= c < self.gridSize:
            if self.grid[r][c] != -1:
                return True
        return False