import heapq

def is_solvable(puzzle):
    """Checks whether the given puzzle is solvable."""
    inversions = 0
    filtered_puzzle = [x for x in puzzle if x != 0]
    for i in range(len(filtered_puzzle)):
        for j in range(i + 1, len(filtered_puzzle)):
            if filtered_puzzle[i] > filtered_puzzle[j]:
                inversions += 1
    return inversions % 2 == 0

def make_move(state, zero_index, target_index):
    """Make a move by swapping the blank tile with the target tile."""
    next_state = list(state)
    next_state[zero_index], next_state[target_index] = next_state[target_index], next_state[zero_index]
    return tuple(next_state)

def ucs(initial, goal):
    """Performs uniform cost search."""
    if not is_solvable(initial):
        return None
    
    # Initialize the priority queue with the initial state
    heap = [(0, tuple(initial), [])]  # (cost, state, path)
    
    # Set to track visited states
    visited = set()
    
    while heap:
        # Pop the state with the lowest cost
        cost, current, path = heapq.heappop(heap)
        
        # Check if the current state matches the goal state
        if current == tuple(goal):
            return path
        
        # If the state has been visited, skip it
        if current in visited:
            continue
        
        # Mark the current state as visited
        visited.add(current)
        
        # Get the index of the blank tile (0)
        zero_index = current.index(0)
        x, y = divmod(zero_index, 3)
        
        # Define possible moves as (target row, target column) and their respective indices
        possible_moves = [
            (x + 1, y, zero_index + 3),  # Down
            (x - 1, y, zero_index - 3),  # Up
            (x, y + 1, zero_index + 1),  # Right
            (x, y - 1, zero_index - 1)   # Left
        ]
        
        # Explore each possible move
        for x2, y2, target_index in possible_moves:
            # Check if the move is within bounds
            if 0 <= x2 < 3 and 0 <= y2 < 3:
                # Make the move
                next_state = make_move(current, zero_index, target_index)
                
                # Create the next path by adding the move
                next_path = path + [(zero_index, target_index)]
                
                # Calculate the new cost (assuming uniform cost of 1 per move)
                next_cost = cost + 1
                
                # Push the new state and its cost to the priority queue
                heapq.heappush(heap, (next_cost, next_state, next_path))
    
    # If no solution is found, return None
    return None

if __name__ == '__main__':
    initial = [1, 2, 3, 0, 4, 6, 7, 5, 8]
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    path = ucs(initial, goal)
    
    if path is not None:
        print("Solution found!")
        print(f"Number of moves: {len(path)}")
        
        # Display initial state
        print("\nInitial state:")
        for i in range(3):
            print(initial[i * 3:i * 3 + 3])
        
        # Apply each move to the puzzle and print the state
        current_state = initial[:]
        for step, (zero_index, target_index) in enumerate(path, start=1):
            current_state[zero_index], current_state[target_index] = current_state[target_index], current_state[zero_index]
            
            print(f"\nStep {step}:")
            for i in range(3):
                print(current_state[i * 3:i * 3 + 3])
    else:
        print("No solution found.")