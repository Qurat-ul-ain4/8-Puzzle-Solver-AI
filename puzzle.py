class Puzzle:

    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def get_neighbors(self, state):

        neighbors = []

        index = state.index(0)

        row = index // 3
        col = index % 3

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in moves:

            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:

                new_index = new_row * 3 + new_col

                new_state = state[:]

                new_state[index], new_state[new_index] = new_state[new_index], new_state[index]

                neighbors.append(new_state)

        return neighbors