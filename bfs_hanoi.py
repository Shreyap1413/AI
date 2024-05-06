from collections import deque

def hanoi_bfs(n, source, target, aux):
    def move_disk(disk, source, target):
        print(f"Move disk {disk} from {source} to {target}")

    def bfs(n, source, target, aux):
        queue = deque([(n, source, target, aux)])
        while queue:
            state = queue.popleft()
            if state[0] == 1:
                move_disk(state[0], state[1], state[2])
            else:
                queue.append((state[0]-1, state[1], state[3], state[2]))
                queue.append((1, state[1], state[2], state[3]))
                queue.append((state[0]-1, state[3], state[2], state[1]))

    print("Initial state:")
    print(f"Source: {source}, Target: {target}, Auxiliary: {aux}")
    bfs(n, source, target, aux)
    print("Tower of Hanoi problem solved!")

# Take user input for the number of disks and the towers
n = int(input("Enter the number of disks (min 3): "))
source = input("Enter the source tower (A, B, or C): ")
target = input("Enter the target tower (A, B, or C): ")
aux = input("Enter the auxiliary tower (A, B, or C): ")

# Test the function with user input
hanoi_bfs(n, source, target, aux)
