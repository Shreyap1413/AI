def manhattan_distance(puzzle, goal):
    """Calculates the Manhattan distance heuristic."""
    distance = 0
    for i in range(9):
        if puzzle[i] == 0 or goal[i] == 0:
            continue
        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(puzzle.index(goal[i]), 3)
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

def dls(current, goal, depth, path, visited):
    """Performs a depth-limited search up to a specified depth."""
    if depth == 0:
        if current == goal:
            return path
        return None
    if tuple(current) in visited:
        return None
    visited.add(tuple(current))
    
    index = current.index(0)
    x, y = divmod(index, 3)
    
    moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    
    for x2, y2 in moves:
        if 0 <= x2 < 3 and 0 <= y2 < 3:
            next_index = x2 * 3 + y2
            next_puzzle = list(current)
            next_puzzle[index], next_puzzle[next_index] = next_puzzle[next_index], next_puzzle[index]
            next_path = path + [(x, y, x2, y2)]
            
            result = dls(next_puzzle, goal, depth - 1, next_path, visited)
            if result is not None:
                return result
    return None

def iddfs(initial, goal):
    """Performs iterative deepening depth-first search."""
    if not is_solvable(initial):
        return None
    
    depth = 0
    while True:
        visited = set()
        path = dls(initial, goal, depth, [], visited)
        if path is not None:
            return path
        depth += 1

if __name__ == '__main__':
    initial = [1, 2, 3, 0, 4, 6, 7, 5, 8]
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    path = iddfs(initial, goal)
    
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