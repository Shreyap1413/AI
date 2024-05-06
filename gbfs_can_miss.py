from queue import PriorityQueue

# Heuristic function to estimate the cost of reaching the goal state from the current state
def heuristic(state):
    m_left, c_left, b_pos, m_right, c_right = state
    return (m_left + c_left - 2) // 2 + (m_right + c_right - 2) // 2

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

# Greedy Best-First Search algorithm
def gbfs(start_state):
    frontier = PriorityQueue()  # Priority queue to explore states based on heuristic values
    frontier.put((heuristic(start_state), [start_state]))  # Insert the initial state with its heuristic value
    explored = set()
    
    while not frontier.empty():
        _, path = frontier.get()  # Get the state with the lowest heuristic value from the priority queue
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
                frontier.put((heuristic(next_state), new_path))  # Insert the new state with its heuristic value into the priority queue
    
    # If no solution is found, return None
    return None

# Testing the algorithm with the initial state (3, 3, 'left', 0, 0)
start_state = (3, 3, 'left', 0, 0)
path = gbfs(start_state)

# Printing the path from the initial state to the goal state
if path:
    for state in path:
        print(state)
else:
    print("No solution found.")