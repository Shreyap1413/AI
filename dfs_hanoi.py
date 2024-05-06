def hanoi_dfs(n, source, target, aux):
    def move_disk(disk, source, target):
        print(f"Move disk {disk} from {source} to {target}")

    def dfs(n, source, target, aux):
        if n == 1:
            move_disk(n, source, target)
        else:
            dfs(n - 1, source, aux, target)
            move_disk(n, source, target)
            dfs(n - 1, aux, target, source)

    print("Initial state:")
    print(f"Source: {source}, Target: {target}, Auxiliary: {aux}")
    dfs(n, source, target, aux)
    print("Tower of Hanoi problem solved!")

# Take user input for the number of disks and the towers
n = int(input("Enter the number of disks (min 3): "))
source = input("Enter the source tower (A, B, or C): ")
target = input("Enter the target tower (A, B, or C): ")
aux = input("Enter the auxiliary tower (A, B, or C): ")

# Test the function with user input
hanoi_dfs(n, source, target, aux)
