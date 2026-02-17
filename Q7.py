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


    def visualizeSearch(self, frontier, explored, title, path=None):
        if not mat.get_fignums(): return False 
        mat.clf()
        mat.imshow(self.grid, cmap='Pastel1')

        for r in range(self.gridSize):
            for c in range(self.gridSize):
                if self.grid[r][c] == -1:
                    mat.text(c, r, "-1", va='center', ha='center', color='black', bbox=dict(facecolor='red', boxstyle='square,pad=1.5'))
                else:
                    mat.text(c, r, "0", va='center', ha='center', color='black', alpha=0.6)

        for node in explored:
            mat.scatter(node[1], node[0], color='green', marker='s', s=1300)

        for item in frontier:
            nodePos = None
            if isinstance(item, tuple):
                if isinstance(item[0], int) and isinstance(item[1], int): nodePos = item
                elif len(item) == 2 and isinstance(item[1], tuple): nodePos = item[1]
            if nodePos:
                mat.scatter(nodePos[1], nodePos[0], color='yellow', marker='s', s=1300)

        if path:
            rows, cols = zip(*path)
            mat.plot(cols, rows, color='black', linewidth=10)

        mat.text(self.start[1], self.start[0], 'S', color='white', weight='bold', ha='center', va='center', bbox=dict(facecolor='purple' ,boxstyle='square,pad=1.5'))
        mat.text(self.target[1], self.target[0], 'G', color='white', weight='bold', ha='center', va='center', bbox=dict(facecolor='blue', boxstyle='square,pad=1.5'))
        mat.title(f"Algorithm: {title}")
        mat.pause(0.01) 
        return True