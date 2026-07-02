from puzzle import Puzzle
from bfs import bfs
from dfs import dfs
from astar import astar
import time

initial_state = [1, 2, 3,
                 4, 0, 6,
                 7, 5, 8]

goal_state = [1, 2, 3,
              4, 5, 6,
              7, 8, 0]

puzzle = Puzzle(initial_state, goal_state)

print("8 Puzzle Solver")
print("1. BFS")
print("2. DFS")
print("3. A*")

choice = input("Enter choice: ")

start_time = time.time()

if choice == '1':
    path, nodes = bfs(puzzle)
    algorithm = "BFS"

elif choice == '2':
    path, nodes = dfs(puzzle)
    algorithm = "DFS"

elif choice == '3':
    path, nodes = astar(puzzle)
    algorithm = "A*"

else:
    print("Invalid Choice")
    exit()

end_time = time.time()

if path:
    print("\nSolution Found!\n")

    print(f"Algorithm Used: {algorithm}")
    print(f"Total Moves: {len(path) - 1}")
    print(f"Nodes Expanded: {nodes}")
    print(f"Execution Time: {end_time - start_time:.5f} seconds")

    print("\nSolution Path:\n")

    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()

else:
    print("No Solution Found")