import random

population = []

for i in range(4):
    chromosome = ''.join(random.choice('01') for _ in range(5))
    population.append(chromosome)

print("Initial Population:", population)

# Fitness function
def fitness(x):
    return x ** 2

# Genetic Algorithm
for generation in range(10):

    # Selection: Select the best two parents
    sorted_population = sorted(
        population,
        key=lambda c: fitness(int(c, 2)),
        reverse=True
    )

    parent1 = sorted_population[0]
    parent2 = sorted_population[1]

    # Crossover: Exchange parts of parents
    point = random.randint(1, 4)

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    # Mutation: Flip a random bit in each child
    child1 = list(child1)
    position = random.randint(0, 4)
    child1[position] = '1' if child1[position] == '0' else '0'
    child1 = ''.join(child1)

    child2 = list(child2)
    position = random.randint(0, 4)
    child2[position] = '1' if child2[position] == '0' else '0'
    child2 = ''.join(child2)

    # Create new population
    population = [parent1, parent2, child1, child2]

    # Find best solution
    best = max(population, key=lambda c: fitness(int(c, 2)))

    x = int(best, 2)

    print("Generation:", generation + 1,
          "| Best chromosome:", best,
          "| x:", x,
          "| Fitness:", fitness(x))

print("\nFinal Best Solution:", x)