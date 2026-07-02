from collections import deque

def bfs(puzzle):
    queue = deque([(puzzle.initial, [puzzle.initial])])
    visited = set()
    nodes_expanded = 0

    while queue:
        state, path = queue.popleft()
        if state == puzzle.goal:
            return path, nodes_expanded

        visited.add(tuple(state))
        nodes_expanded += 1

        for neighbor in puzzle.get_neighbors(state):
            if tuple(neighbor) not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None, nodes_expanded
