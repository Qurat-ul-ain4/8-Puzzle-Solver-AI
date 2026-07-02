def dfs(puzzle):
    stack = [(puzzle.initial, [puzzle.initial])]
    visited = set()
    nodes_expanded = 0

    while stack:
        state, path = stack.pop()
        if state == puzzle.goal:
            return path, nodes_expanded

        visited.add(tuple(state))
        nodes_expanded += 1

        for neighbor in puzzle.get_neighbors(state):
            if tuple(neighbor) not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None, nodes_expanded
