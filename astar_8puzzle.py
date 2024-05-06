import heapq

def manhattan_distance(puzzle, goal):
    """Calculates the Manhattan distance heuristic."""
    distance = 0
    for i in range(9):
        if puzzle[i] == 0 or goal[i] == 0:
            continue
        current_pos = puzzle.index(goal[i])
        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(current_pos, 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def is_solvable(puzzle):
    """Checks whether the given puzzle is solvable."""
    inversions = 0
    filtered_puzzle = [x for x in puzzle if x != 0]
    for i in range(len(filtered_puzzle)):
        for j in range(i + 1, len(filtered_puzzle)):
            if filtered_puzzle[i] > filtered_puzzle[j]:
                inversions += 1
    return inversions % 2 == 0

def a_star_search(initial, goal):
    """Performs A* search to solve the 8-puzzle game."""
    if not is_solvable(initial):
        return None
    
    # Initialize the priority queue (heap) with the initial state
    heap = [(manhattan_distance(initial, goal), 0, tuple(initial), [])] # (f, g, state, path)
    
    # Set to track visited states
    visited = set()
    
    while heap:
        # Pop the state with the lowest estimated cost (f) from the heap
        _, g, current_state, path = heapq.heappop(heap)
        
        # Check if the current state matches the goal state
        if current_state == tuple(goal):
            return path
        
        # If the state has been visited, skip it
        if current_state in visited:
            continue
        
        # Mark the current state as visited
        visited.add(current_state)
        
        # Find the index of the blank tile (0)
        zero_index = current_state.index(0)
        x, y = divmod(zero_index, 3)
        
        # Possible moves (down, up, right, left)
        moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        
        # Explore each possible move
        for x2, y2 in moves:
            # Check if the move is within bounds
            if 0 <= x2 < 3 and 0 <= y2 < 3:
                # Calculate the index of the target tile
                next_index = x2 * 3 + y2
                
                # Create a copy of the current state and swap the blank tile with the target tile
                next_state = list(current_state)
                next_state[zero_index], next_state[next_index] = next_state[next_index], next_state[zero_index]
                
                # Create the next path
                next_path = path + [(x, y, x2, y2)]
                
                # Calculate the new cost (g) of the path
                next_g = g + 1
                
                # Calculate the heuristic (h) for the new state
                next_h = manhattan_distance(next_state, goal)
                
                # Calculate the estimated cost (f = g + h)
                next_f = next_g + next_h
                
                # Push the new state to the heap with its estimated cost, cost so far, state, and path
                heapq.heappush(heap, (next_f, next_g, tuple(next_state), next_path))
    
    # If no solution is found, return None
    return None

if __name__ == '__main__':
    initial = [1, 2, 3, 0, 4, 6, 7, 5, 8]
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    path = a_star_search(initial, goal)
    
    if path is not None:
        print("Solution found!")
        print(f"Number of moves: {len(path)}")
        
        # Display initial state
        print("\nInitial state:")
        for i in range(3):
            print(initial[i * 3:i * 3 + 3])
        
        # Apply each move to the puzzle and print the state
        for step, (x1, y1, x2, y2) in enumerate(path, start=1):
            zero_index = x1 * 3 + y1
            move_index = x2 * 3 + y2
            initial[zero_index], initial[move_index] = initial[move_index], initial[zero_index]
            print(f"\nStep {step}:")
            for i in range(3):
                print(initial[i * 3:i * 3 + 3])
    else:
        print("No solution found.")