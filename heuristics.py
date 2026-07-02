def manhattan_distance(state, goal):
    distance = 0
    for num in range(1, 9):
        current_index = state.index(num)
        goal_index = goal.index(num)
        x1, y1 = divmod(current_index, 3)
        x2, y2 = divmod(goal_index, 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance
