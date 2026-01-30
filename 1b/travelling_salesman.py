import random
import math


# 1. Here, we first have to generate random cities

def generate_cities(n):

    cities = []
    for _ in range(n):
        x = random.uniform(0, 1000)
        y = random.uniform(0, 1000)
        cities.append((x, y))
    return cities



# 2. Euclidean distance between two cities

def euclidean_distance(city1, city2):

    return math.sqrt((city1[0] - city2[0]) ** 2 +
                     (city1[1] - city2[1]) ** 2)



# Total distance of a tour

def total_tour_distance(tour, cities):

    distance = 0
    n = len(tour)

    for i in range(n):
        current_city = cities[tour[i]]
        next_city = cities[tour[(i + 1) % n]]
        distance += euclidean_distance(current_city, next_city)

    return distance



# Swapping neighborhood

def swap_neighbor(tour):

    new_tour = tour[:]
    i, j = random.sample(range(len(tour)), 2)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour



# 2-opt neighborhood

def two_opt_neighbor(tour):
    """
    Reverse a segment of the tour.
    """
    new_tour = tour[:]
    i, j = sorted(random.sample(range(len(tour)), 2))
    new_tour[i:j] = reversed(new_tour[i:j])
    return new_tour



# 2. Implementing Simulated Annealing with selectable cooling


def simulated_annealing(cities, cooling_type="exponential"):
    """
    Solve TSP using Simulated Annealing.

    cooling_type:
        "exponential" -> T = T * alpha
        "linear"      -> T = T - beta
    """

    # Initial temperature
    T = 1000
    T_min = 0.001

    # Cooling parameters
    alpha = 0.995   # exponential cooling rate
    beta = 0.05     # linear cooling rate

    max_iterations = 100000

    # Initial random tour
    n = len(cities)
    current_tour = list(range(n))
    random.shuffle(current_tour)

    current_cost = total_tour_distance(current_tour, cities)

    best_tour = current_tour[:]
    best_cost = current_cost

    # Main SA loop
    for iteration in range(max_iterations):

        if T < T_min:
            break

        # Generate neighbor (randomly choose move)
        if random.random() < 0.5:
            new_tour = swap_neighbor(current_tour)
        else:
            new_tour = two_opt_neighbor(current_tour)

        new_cost = total_tour_distance(new_tour, cities)
        delta = new_cost - current_cost

        # Acceptance rule
        if delta < 0 or random.random() < math.exp(-delta / T):
            current_tour = new_tour
            current_cost = new_cost

        # Update best solution
        if current_cost < best_cost:
            best_tour = current_tour[:]
            best_cost = current_cost

        # Cooling schedule
        if cooling_type == "exponential":
            T = T * alpha
        elif cooling_type == "linear":
            T = T - beta

    return best_tour, best_cost



# Run both cooling schedules

if __name__ == "__main__":
    N = 30
    cities = generate_cities(N)

    print("Running Simulated Annealing with Exponential Cooling...")
    tour_exp, dist_exp = simulated_annealing(cities, "exponential")
    print("Best distance (Exponential):", dist_exp)

    print("\nRunning Simulated Annealing with Linear Cooling...")
    tour_lin, dist_lin = simulated_annealing(cities, "linear")
    print("Best distance (Linear):", dist_lin)



# Here,
# State: A permutation of cities
# Objective Function: Total Euclidean distance of the tour
# Neighborhood: Swap and 2-opt
# Acceptance Rule: Metropolis criterion
# Cooling Schedule: Exponential cooling
# Stopping Criteria: Temperature threshold or max iterations


# The stopping criteria are reaching a minimum temperature threshold (T < T_min) or exceeding the maximum number of iterations, 
# whichever occurs first.