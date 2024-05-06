from collections import deque

# Function to check if a state is valid
def is_valid(state):
    m_left, c_left, b_pos, m_right, c_right = state
    # Check if any number is negative or exceeds the initial count of 3
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 3 or c_left > 3 or m_right > 3 or c_right > 3:
        return False
    # Check if there are more cannibals than missionaries on either side
    if (c_left > m_left > 0) or (c_right > m_right > 0):
        return False
    return True

# Function to generate the next valid states from the current state
def next_states(state):
    m_left, c_left, b_pos, m_right, c_right = state
    if b_pos == 'left':
        moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
        next_states = [(m_left - m, c_left - c, 'right', m_right + m, c_right + c) for m, c in moves]
    else:
        moves = [(-2, 0), (0, -2), (-1, -1), (-1, 0), (0, -1)]
        next_states = [(m_left + m, c_left + c, 'left', m_right - m, c_right - c) for m, c in moves]
    return [next_state for next_state in next_states if is_valid(next_state)]

# Breadth-First Search algorithm
def bfs(start_state):
    frontier = deque()
    frontier.append([start_state])
    explored = set()
    
    while frontier:
        path = frontier.popleft()
        current_state = path[-1]
        
        # Check if the current state is the goal state
        if current_state == (0, 0, 'right', 3, 3):
            return path
        
        # Generate the next valid states from the current state
        for next_state in next_states(current_state):
            if next_state not in explored:
                new_path = path + [next_state]
                frontier.append(new_path)
                explored.add(next_state)
                
    # Return None if no solution is found
    return None

# Testing the algorithm with the initial state (3, 3, 'left', 0, 0)
start_state = (3, 3, 'left', 0, 0)
path = bfs(start_state)

# Printing the path from the initial state to the goal state
if path:
    for state in path:
        print(state)
else:
    print("No solution found.")