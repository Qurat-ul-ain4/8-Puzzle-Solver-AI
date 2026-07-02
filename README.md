# 8-Puzzle Solver (AI Semester Project) 🧩

This repository contains the implementation of an **8-Puzzle Solver** developed as a semester project for the Artificial Intelligence course at **UET Mardan**.

## 📝 Project Overview
The 8-puzzle is a sliding puzzle that consists of a frame of numbered square tiles in random order with one tile missing. The object of the puzzle is to place the tiles in order by making sliding moves that use the empty space.

### 🧠 Algorithms Implemented
1. **BFS (Breadth First Search):** Explores all nodes at the present depth level before moving to nodes at the next depth level.
2. **DFS (Depth First Search):** Explores as far as possible along each branch before backtracking.
3. **A* Search:** An informed search algorithm that uses heuristics to find the shortest path efficiently.
   - *Heuristics Used:* Manhattan Distance / Misplaced Tiles.

---

## 📂 Project Structure & Files
*   `main.py` - The main execution entry point.
*   `puzzle.py` - Defines the puzzle state and logic.
*   `bfs.py` - Breadth-First Search algorithm implementation.
*   `dfs.py` - Depth-First Search algorithm implementation.
*   `astar.py` - A* Search algorithm implementation.
*   `heuristics.py` - Contains heuristic functions for A* Search.

---

## 📈 Performance Comparison & Results
The project includes a detailed analysis comparing **BFS, DFS, and A\*** based on:
*   Time Complexity (Execution Time)
*   Space Complexity (Nodes Explored)
*   Optimality of the solution path.

## 🚀 How to Run
1. Clone the repository.
2. Run `python main.py` in your terminal.