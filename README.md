# AI Pathfinder - Uninformed Search Algorithms Visualization

## Project Description
This project implements an **AI Pathfinder** that visualizes six fundamental **Uninformed Search Algorithms** navigating a 10x10 grid environment. The agent starts at a designated **Start Point (S)** and attempts to find the optimal path to a **Target Point (T)** while avoiding static obstacles (walls).

The core feature of this project is the **GUI Visualization** using `matplotlib`, which demonstrates the "thinking process" of each algorithm step-by-step in real-time.

## Features
- **Grid Environment:** A 10x10 grid with static walls.
- **Real-Time Visualization:** Animates the search process, showing:
  - **Frontier Nodes** (Yellow): Nodes currently in the queue/stack waiting to be explored.
  - **Explored Nodes** (Green): Nodes that have already been visited.
  - **Final Path** (Black): The successful route from Start to Target.
- **Strict Movement Order:** The agent explores neighbors in a specific Clockwise order: **Up, Right, Bottom, Bottom-Right, Left, Top-Left**.

## Algorithms Implemented
1. **Breadth-First Search (BFS):** Explores all neighbors at the present depth prior to moving on to the nodes at the next depth level. Guarantees the shortest path.
2. **Depth-First Search (DFS):** Explores as far as possible along each branch before backtracking.
3. **Uniform-Cost Search (UCS):** Expands the node with the lowest path cost (uses a Priority Queue).
4. **Depth-Limited Search (DLS):** A version of DFS with a predetermined depth limit to prevent infinite loops.
5. **Iterative Deepening DFS (IDDFS):** repeatedly runs DLS with increasing depth limits until the target is found.
6. **Bidirectional Search:** Runs two simultaneous searches (one from Start, one from Target) and stops when they meet in the middle.

## Technologies Used
- **Language:** Python 3.x
- **Libraries:**
  - `matplotlib`: For the Graphical User Interface (GUI) and animation.
  - `collections`: For using `deque` (efficient queues).
  - `heapq`: For implementing Priority Queues in UCS.

## How to Run
1. **Clone the Repository:**
   ```bash
   git clone: https://github.com/shaheer-sa/Ai-PathFinder.git
Install Dependencies:
Make sure you have Python installed. Then install matplotlib:

Bash
pip install matplotlib
Run the Script:

Bash
python Q7.py

Select an Algorithm:
A menu will appear in the terminal. Enter the number corresponding to the algorithm you want to visualize (e.g., 1 for BFS).

Visualization Example
The GUI uses the following color code:

Red: Static Walls (Obstacles)

Green: Explored Nodes

Yellow: Frontier Nodes (Queue/Stack)

Black Line: Final Path

Purple/Blue Blocks: Start and Goal positions

Requirements
Python 3.6 or higher

Matplotlib library

Author:

Muhammad Shaheer Ahmad
Muhammad Ibrahim Manzoor

24F-0538
24F-0662