import random

# Define the cities and their coordinates
cities = {
    'A': (0, 0),
    'B': (5, 2),
    'C': (6, 3),
    'D': (3, 4),
    'E': (2, 5)
}

# Number of iterations and population size
num_iterations = 100
pop_size = 50

# Define functions for distance and route distance
dist = lambda c1, c2: ((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)**0.5
route_dist = lambda route: sum(dist(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1))

# Create initial population
population = [random.sample(list(cities.keys()), len(cities)) for _ in range(pop_size)]

# Perform the genetic algorithm iterations
for _ in range(num_iterations):
    # Select two parents randomly
    p1, p2 = random.sample(population, 2)
    
    # Define the crossover range
    start, end = sorted(random.sample(range(len(cities)), 2))
    
    # Perform crossover
    child = p1[start:end] + [c for c in p2 if c not in p1[start:end]]
    
    # Perform mutation with a probability of 0.1
    if random.random() < 0.1:
        idx1, idx2 = random.sample(range(len(child)), 2)
        child[idx1], child[idx2] = child[idx2], child[idx1]
    
    # Replace the worst route in the population with the new child
    population.remove(max(population, key=route_dist))
    population.append(child)

# Find the best route in the population
best_route = min(population, key=route_dist)
print("Best route:", best_route, "\nTotal distance:", route_dist(best_route))