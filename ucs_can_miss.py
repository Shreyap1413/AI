from queue import PriorityQueue

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

# Uniform Cost Search algorithm
def ucs(start_state):
    frontier = PriorityQueue()  # Priority queue to explore states with lowest cost first
    frontier.put((0, [start_state]))  # Insert the initial state with cost 0
    explored = set()
    
    while not frontier.empty():
        cost, path = frontier.get()  # Get the state with the lowest cost from the priority queue
        current_state = path[-1]
        
        # If the current state is the goal state, return the path
        if current_state == (0, 0, 'right', 3, 3):
            return path
        
        # If the current state has not been explored, process it
        if current_state not in explored:
            explored.add(current_state)
            
            # Generate the next valid states from the current state
            for next_state in next_states(current_state):
                new_path = path + [next_state]
                new_cost = cost + 1  # Uniform cost for each move
                frontier.put((new_cost, new_path))  # Insert the new state with updated cost into the priority queue
    
    # If no solution is found, return None
    return None

# Testing the algorithm with the initial state (3, 3, 'left', 0, 0)
start_state = (3, 3, 'left', 0, 0)
path = ucs(start_state)

# Printing the path from the initial state to the goal state
if path:
    for state in path:
        print(state)
else:
    print("No solution found.")