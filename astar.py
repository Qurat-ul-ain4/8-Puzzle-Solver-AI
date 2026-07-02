import heapq
from heuristics import manhattan_distance

def astar(puzzle):
    heap = []
    heapq.heappush(heap, (0, puzzle.initial, [puzzle.initial]))
    visited = set()
    nodes_expanded = 0

    while heap:
        cost, state, path = heapq.heappop(heap)
        if state == puzzle.goal:
            return path, nodes_expanded

        visited.add(tuple(state))
        nodes_expanded += 1

        for neighbor in puzzle.get_neighbors(state):
            if tuple(neighbor) not in visited:
                g = len(path)
                h = manhattan_distance(neighbor, puzzle.goal)
                f = g + h
                heapq.heappush(heap, (f, neighbor, path + [neighbor]))

    return None, nodes_expanded
