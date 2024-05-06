# Function to check if a state is valid
def is_valid(state):
    m_left, c_left, b_pos, m_right, c_right = state
    # Check if any count is negative
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    # Check if any count is greater than the maximum value (3)
    if m_left > 3 or c_left > 3 or m_right > 3 or c_right > 3:
        return False
    # Check if cannibals outnumber missionaries on either side
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
    return [state for state in next_states if is_valid(state)]

# Depth-First Search algorithm with depth limit
def dfs_limit(start_state, depth_limit):
    frontier = []  # Use a stack for DFS
    frontier.append([start_state])
    explored = set()
    
    while frontier:
        # Pop the last element from the stack
        path = frontier.pop()
        current_state = path[-1]
        
        # Check if the current state is the goal state
        if current_state == (0, 0, 'right', 3, 3):
            return path
        
        # Check the depth limit
        if len(path) <= depth_limit:
            # Generate the next valid states from the current state
            for next_state in next_states(current_state):
                if next_state not in explored:
                    new_path = path + [next_state]
                    frontier.append(new_path)
                    explored.add(next_state)
                    
    return None

# Iterative Deepening Depth-First Search algorithm
def iddfs(start_state):
    depth_limit = 0
    while True:
        # Perform DFS with the current depth limit
        result = dfs_limit(start_state, depth_limit)
        
        # If a result is found, return the result
        if result:
            return result
        
        # Increase the depth limit
        depth_limit += 1

# Testing the algorithm with the initial state (3, 3, 'left', 0, 0)
start_state = (3, 3, 'left', 0, 0)
path = iddfs(start_state)

# Printing the path from the initial state to the goal state
if path:
    for state in path:
        print(state)
else:
    print("No solution found.")