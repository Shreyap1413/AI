from queue import PriorityQueue

# Heuristic function to estimate the cost of reaching the goal state from the current state
def heuristic(state):
    m_left, c_left, b_pos, m_right, c_right = state
    return (m_left + c_left - 2) // 2 + (m_right + c_right - 2) // 2

# Function to check if a state is valid
def is_valid(state):
    m_left, c_left, b_pos, m_right, c_right = state
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 3 or c_left > 3 or m_right > 3 or c_right > 3:
        return False
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

# A* Search algorithm
def astar(start_state):
    frontier = PriorityQueue()  # Priority queue to explore states based on the sum of cost and heuristic value
    frontier.put((0, [start_state]))  # Insert the initial state with cost 0
    explored = set()
    
    while not frontier.empty():
        cost, path = frontier.get()  # Get the state with lowest cost from the priority queue
        current_state = path[-1]
        
        # Check if the current state is the goal state
        if current_state == (0, 0, 'right', 3, 3):
            return path
        
        # If the current state is not explored, add it to the explored set
        if current_state not in explored:
            explored.add(current_state)
            
            # Generate the next valid states from the current state
            for next_state in next_states(current_state):
                new_cost = len(path) - 1  # Uniform cost for each move
                new_path = path + [next_state]
                frontier.put((new_cost + heuristic(next_state), new_path))  # Insert the new state with its priority into the priority queue
    
    return None

# Testing the algorithm with the initial state (3, 3, 'left', 0, 0)
start_state = (3, 3, 'left', 0, 0)
path = astar(start_state)

# Printing the path from the initial state to the goal state
if path:
    for state in path:
        print(state)
else:
    print("No solution found.")