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
    
    

    def getPath(self, parent, endNode):
        route = []
        curr = endNode
        while curr is not None:
            route.append(curr)
            curr = parent.get(curr)
        return route[::-1]


    # -------- ALGORITHMS --------



    # -------- BFS ---------

    def BFS(self):
        queue = collections.deque([self.start])
        parents = {self.start: None}
        explored = []
        
        while queue:
            curr = queue.popleft()
            if curr == self.target:
                self.visualizeSearch(list(queue), explored, "BFS", self.getPath(parents, curr))
                return True
            
            if curr not in explored:
                explored.append(curr)
                for row, col in self.moveOrder:
                    neighbor = (curr[0] + row, curr[1] + col)
                    if self.isValidMove(neighbor[0], neighbor[1]) and neighbor not in parents:
                        parents[neighbor] = curr
                        queue.append(neighbor)
                
                if not self.visualizeSearch(list(queue), explored, "BFS"):
                    return False
        return False
    
    
    # -------- DFS ---------

    def DFS(self, limit=None):
        stack = [(self.start, 0)]
        parents = {self.start: None}
        explored = []
        title=""
        if limit==None:
            title="DFS"
        else:
            title="DLS"
        
        while stack:
            curr, depth = stack.pop()
            if curr == self.target:
                self.visualizeSearch([s[0] for s in stack], explored, title, self.getPath(parents, curr))
                return True
            
            if curr not in explored:
                if limit is None or depth < limit:
                    explored.append(curr)
                    for dr, dc in reversed(self.moveOrder):
                        neighbor = (curr[0] + dr, curr[1] + dc)
                        if self.isValidMove(neighbor[0], neighbor[1]) and neighbor not in parents:
                            parents[neighbor] = curr
                            stack.append((neighbor, depth + 1))
                    
                    if not self.visualizeSearch([s[0] for s in stack], explored, title):
                        return False
        return False
    

    # -------- IDS ---------

    def IDS(self):
        for depth in range(self.gridSize * self.gridSize):
            print(f"Current Depth Limit: {depth}")
            
            found = self.DFS(limit=depth)
            
            if found:
                return True
            
            if not mat.get_fignums(): 
                return False 
            
        return False


    # -------- UCS ---------

    def UCS(self):
        pQueue = [(0, self.start)] 
        cost = {self.start: 0} # Dictionary storing costs
        parent = {self.start: None}
        explored = []
        
        while pQueue:
            # FIX: Renamed 'cost' to 'currentCost' to avoid overwriting the dictionary
            currentCost, curr = heapq.heappop(pQueue)
            
            if curr == self.target:
                self.visualizeSearch(list(pQueue), explored, "UCS", self.getPath(parent, curr))
                return True
            
            if curr not in explored:
                explored.append(curr)
                for row, col in self.moveOrder:
                    neighbor = (curr[0] + row, curr[1] + col)
                    
                    # FIX: Use 'currentCost' here
                    newCost = currentCost + 1
                    
                    if self.isValidMove(neighbor[0], neighbor[1]):
                        if neighbor not in cost or newCost < cost[neighbor]:
                            cost[neighbor] = newCost
                            parent[neighbor] = curr
                            heapq.heappush(pQueue, (newCost, neighbor))
                
                if not self.visualizeSearch(list(pQueue), explored, "UCS"):
                    return False
                


# -------- Bi-Directional ---------

    def biDirectional(self):
        fQueue, bQueue = collections.deque([self.start]), collections.deque([self.target])
        fParents, bParents = {self.start: None}, {self.target: None}
        fExplored, bExplored = [], []

        while fQueue and bQueue:
            # Forward
            currNodeF = fQueue.popleft()
            fExplored.append(currNodeF)
            for row, col in self.moveOrder:
                adj = (currNodeF[0] + row, currNodeF[1] + col)
                if self.isValidMove(adj[0], adj[1]) and adj not in fParents:
                    fParents[adj] = currNodeF
                    fQueue.append(adj)
                    if adj in bParents:
                        path = self.getPath(fParents, adj) + self.getPath(bParents, adj)[::-1][1:]
                        self.visualizeSearch(list(fQueue)+list(bQueue), fExplored+bExplored, "Bi-Directional", path)
                        return True
            
            if not self.visualizeSearch(list(fQueue)+list(bQueue), fExplored+bExplored, "Bi-Directional"):
                return False

            # Backward
            currNodeB = bQueue.popleft()
            bExplored.append(currNodeB)
            for row, col in self.moveOrder:
                adj = (currNodeB[0] + row, currNodeB[1] + col)
                if self.isValidMove(adj[0], adj[1]) and adj not in bParents:
                    bParents[adj] = currNodeB
                    bQueue.append(adj)
                    if adj in fParents:
                        path = self.getPath(fParents, adj) + self.getPath(bParents, adj)[::-1][1:]
                        self.visualizeSearch(list(fQueue)+list(bQueue), fExplored+bExplored, "Bi-Directional", path)
                        return True
            
            if not self.visualizeSearch(list(fQueue)+list(bQueue), fExplored+bExplored, "Bi-Directional"):
                return False

def menuDisplay():
    pathFinder = AiPathfinder()
    while True:
        print("\n --- ALGORITHM MENU ---\n")
        print("1. BFS  2. DFS  3. UCS  4. DLS  5. IDDFS  6. Bidirectional  7. Exit")
        opt = input("Choice: ")
        
        if opt == '7': 
            break
        
        if opt in ['1', '2', '3', '4', '5', '6']:
            mat.figure(figsize=(7, 7)) 
            
            if opt == '1': pathFinder.BFS()
            elif opt == '2': pathFinder.DFS()
            elif opt == '3': pathFinder.UCS()
            elif opt == '4':
                try:
                    limit=int(input("Enter limit: "))
                    pathFinder.DFS(limit=limit)
                except ValueError:
                    print("Please enter a valid number.")
            elif opt == '5': pathFinder.IDS()
            elif opt == '6': pathFinder.biDirectional()
            
            if mat.get_fignums():
                mat.show() 
        else:
             print("Invalid choice!")

if __name__ == "__main__":
    menuDisplay()


