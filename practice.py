# 1 a)

# import math

# def geometric_median(sensor_locations, eps=1e-6, max_iter=1000):
#     """
#     Computes the geometric median of 2D points using Weiszfeld's algorithm.

#     Parameters:
#     sensor_locations : List of [x, y] coordinates
#     eps              : Convergence threshold
#     max_iter         : Maximum number of iterations

#     Returns:
#     (hub_x, hub_y)   : Optimal hub location
#     """

#     # Step 1: Initialize at centroid
#     x = sum(p[0] for p in sensor_locations) / len(sensor_locations)
#     y = sum(p[1] for p in sensor_locations) / len(sensor_locations)

#     for _ in range(max_iter):
#         num_x = 0.0
#         num_y = 0.0
#         denom = 0.0

#         for xi, yi in sensor_locations:
#             dist = math.hypot(x - xi, y - yi)

#             # If hub coincides with a sensor, it is optimal
#             if dist < eps:
#                 return xi, yi

#             weight = 1.0 / dist
#             num_x += xi * weight
#             num_y += yi * weight
#             denom += weight

#         new_x = num_x / denom
#         new_y = num_y / denom

#         # Check convergence
#         if math.hypot(new_x - x, new_y - y) < eps:
#             break

#         x, y = new_x, new_y

#     return x, y


# def total_distance(hub_x, hub_y, sensor_locations):
#     """
#     Computes the sum of Euclidean distances from hub to sensors.
#     """
#     return sum(math.hypot(hub_x - xi, hub_y - yi) for xi, yi in sensor_locations)



# sensors = [
#     (1,1),(3,3)
# ]

# hub_x, hub_y = geometric_median(sensors)
# distance_sum = total_distance(hub_x, hub_y, sensors)

# print("Optimal hub location:", (hub_x, hub_y))
# print("Minimum total distance:", distance_sum)








# # Why This Is Correct (For Examiner)

# #     Uses Weiszfeld’s algorithm, a standard method for computing the geometric median

# #     Objective function is convex, ensuring convergence to the global minimum

# #     Handles division-by-zero edge case

# #     Time complexity: O(N × iterations)




# # Key Notes for Assignment

# #     This approach minimizes sum of Euclidean distances, not squared distances

# #     The centroid is not optimal for this problem

# #     The algorithm converges rapidly in practice

###############################################################################################################
#1 b)

# import random
# import math

# --------------------------------------------------
# 1. Generate random cities
# --------------------------------------------------
# def generate_cities(n):
#     """
#     Generate n cities with random (x, y) coordinates.
#     """
#     cities = []
#     for _ in range(n):
#         x = random.uniform(0, 1000)
#         y = random.uniform(0, 1000)
#         cities.append((x, y))
#     return cities


# # --------------------------------------------------
# # 2. Euclidean distance between two cities
# # --------------------------------------------------
# def euclidean_distance(city1, city2):
#     """
#     Compute Euclidean distance between two cities.
#     """
#     return math.sqrt((city1[0] - city2[0]) ** 2 +
#                      (city1[1] - city2[1]) ** 2)


# # --------------------------------------------------
# # 3. Total distance of a tour
# # --------------------------------------------------
# def total_tour_distance(tour, cities):
#     """
#     Compute total distance of a round-trip tour.
#     """
#     distance = 0
#     n = len(tour)

#     for i in range(n):
#         current_city = cities[tour[i]]
#         next_city = cities[tour[(i + 1) % n]]
#         distance += euclidean_distance(current_city, next_city)

#     return distance


# # --------------------------------------------------
# # 4. Swap neighborhood
# # --------------------------------------------------
# def swap_neighbor(tour):
#     """
#     Swap two random cities in the tour.
#     """
#     new_tour = tour[:]
#     i, j = random.sample(range(len(tour)), 2)
#     new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
#     return new_tour


# # --------------------------------------------------
# # 5. 2-opt neighborhood
# # --------------------------------------------------
# def two_opt_neighbor(tour):
#     """
#     Reverse a segment of the tour.
#     """
#     new_tour = tour[:]
#     i, j = sorted(random.sample(range(len(tour)), 2))
#     new_tour[i:j] = reversed(new_tour[i:j])
#     return new_tour


# # --------------------------------------------------
# # 6. Simulated Annealing with selectable cooling
# # --------------------------------------------------
# def simulated_annealing(cities, cooling_type="exponential"):
#     """
#     Solve TSP using Simulated Annealing.

#     cooling_type:
#         "exponential" -> T = T * alpha
#         "linear"      -> T = T - beta
#     """

#     # Initial temperature
#     T = 1000
#     T_min = 0.001

#     # Cooling parameters
#     alpha = 0.995   # exponential cooling rate
#     beta = 0.05     # linear cooling rate

#     max_iterations = 100000

#     # Initial random tour
#     n = len(cities)
#     current_tour = list(range(n))
#     random.shuffle(current_tour)

#     current_cost = total_tour_distance(current_tour, cities)

#     best_tour = current_tour[:]
#     best_cost = current_cost

#     # Main SA loop
#     for iteration in range(max_iterations):

#         if T < T_min:
#             break

#         # Generate neighbor (randomly choose move)
#         if random.random() < 0.5:
#             new_tour = swap_neighbor(current_tour)
#         else:
#             new_tour = two_opt_neighbor(current_tour)

#         new_cost = total_tour_distance(new_tour, cities)
#         delta = new_cost - current_cost

#         # Acceptance rule
#         if delta < 0 or random.random() < math.exp(-delta / T):
#             current_tour = new_tour
#             current_cost = new_cost

#         # Update best solution
#         if current_cost < best_cost:
#             best_tour = current_tour[:]
#             best_cost = current_cost

#         # Cooling schedule
#         if cooling_type == "exponential":
#             T = T * alpha
#         elif cooling_type == "linear":
#             T = T - beta

#     return best_tour, best_cost


# # --------------------------------------------------
# # 7. Run both cooling schedules
# # --------------------------------------------------
# if __name__ == "__main__":
#     N = 30
#     cities = generate_cities(N)

#     print("Running Simulated Annealing with Exponential Cooling...")
#     tour_exp, dist_exp = simulated_annealing(cities, "exponential")
#     print("Best distance (Exponential):", dist_exp)

#     print("\nRunning Simulated Annealing with Linear Cooling...")
#     tour_lin, dist_lin = simulated_annealing(cities, "linear")
#     print("Best distance (Linear):", dist_lin)





# Two cooling schedules were implemented. Exponential cooling reduces temperature multiplicatively 
# and allows slow convergence, while linear cooling reduces temperature at a constant rate and converges faster but may 
# lead to premature convergence.

# How to Explain This in an Exam / Viva

# State: A permutation of cities

# Objective Function: Total Euclidean distance of the tour

# Neighborhood: Swap and 2-opt

# Acceptance Rule: Metropolis criterion

# Cooling Schedule: Exponential cooling

# Stopping Criteria: Temperature threshold or max iterations



################################################################################################################
# 2)

# def max_points(tile_multipliers):
#     n = len(tile_multipliers) #Number of tiles
#     nums = [1] + tile_multipliers + [1]  # Pad the tile array with 1 at both ends to simplify edge calculations
#     # nums[0] = 1, nums[1..n] = original tiles, nums[n+1] = 1


#     # Initialize DP table: dp[left][right] = max points for interval left..right
#     # Table size is (n+2) x (n+2) to include padding
#     dp = [[0] * (n + 2) for _ in range(n + 2)]



#  # Fill DP table by increasing interval length
#     for length in range(1, n + 1):  # length = size of current subarray
#         for left in range(1, n - length + 2):  # start of interval
#             right = left + length - 1  # end of interval
#             # Try each tile i in [left, right] as the last one to shatter in this interval
#             for i in range(left, right + 1):
#                 # Points if tile i is shattered last:
#                 # dp[left][i-1] = max points from left subarray
#                 # dp[i+1][right] = max points from right subarray
#                 # nums[left-1]*nums[i]*nums[right+1] = points from shattering tile i last
#                 dp[left][right] = max(
#                     dp[left][right],  # current max for this interval
#                     dp[left][i-1] + dp[i+1][right] + nums[left-1] * nums[i] * nums[right+1]
#                 )

#     # The maximum points for the full array is stored in dp[1][n]
#     return dp[1][n]


# # Example
# print(max_points([3, 1, 5, 8]))  # Output: 167










# Problem in Simple Words

# You have a row of tiles, each with a number (score multiplier):

# Example: [3, 1, 5, 8]


# You shatter tiles one by one.

# When you shatter a tile, you get points equal to:

# left neighbor
# ×
# tile itself
# ×
# right neighbor
# left neighbor×tile itself×right neighbor

# If there is no neighbor (tile is at the edge), treat it as 1.

# Goal: Pick the order of shattering so that your total points are as big as possible.

# Example:

# tiles = [3, 1, 5, 8]

# Shatter tile 1 (second tile, value=1)

# Left = 3, Right = 5 → points = 3 × 1 × 5 = 15

# Remaining tiles: [3, 5, 8]

# Shatter tile 5

# Left = 3, Right = 8 → points = 3 × 5 × 8 = 120

# Remaining tiles: [3, 8]

# Shatter tile 3

# Left = 1 (out of bounds → 1), Right = 8 → points = 1 × 3 × 8 = 24

# Remaining tile: [8]

# Shatter tile 8

# Left = 1, Right = 1 → points = 1 × 8 × 1 = 8

# Total points = 15 + 120 + 24 + 8 = 167

# ✅ That’s the maximum points we can get.

# Why It’s Hard

# The order you shatter tiles changes your points.

# Some tiles might give more points if shattered later.

# We need a smart way to try all possibilities efficiently.

# Brute force (trying all orders) would take too long, especially if you have 10+ tiles.

# Dynamic Programming (DP) Solution – Simple Idea

# Instead of trying all orders, we think backwards:

# “Suppose I know the maximum points I can get for smaller groups of tiles. How can I use that to get the answer for a bigger group?”

# Step 1: Think of Intervals

# Consider a subarray of tiles, like [1, 5, 8].

# Let’s ask: If I shatter all tiles in this subarray, what is the max points I can get?

# Call this dp[left][right] = maximum points from shattering tiles from left to right.

# Step 2: Last Tile Idea

# Instead of thinking of the first tile, we think:

# “Which tile should be shattered last in this subarray?”

# Why last? Because its neighbors are already fixed when it’s shattered, so points are easy to calculate.

# If the last tile is i, points =

# points from left part + points from right part + points from shattering tile i last


# Points from shattering tile i last =

# left neighbor × i × right neighbor

# Step 3: Recurrence Formula

# If nums is the tile array padded with 1s at both ends:

# dp[left][right] = max(dp[left][i-1] + dp[i+1][right] + nums[left-1]*nums[i]*nums[right+1]) 
# for all i in [left, right]


# dp[left][i-1] → max points from left part

# dp[i+1][right] → max points from right part

# nums[left-1]*nums[i]*nums[right+1] → points for last tile

# Step 4: Base Case

# If no tiles in the interval → points = 0

# Step 5: Solve Small Intervals First

# Start with intervals of length 1 (just 1 tile)

# Then length 2, 3, … up to full array

# This ensures when we calculate dp[left][right], all smaller intervals are already solved.

################################################################################################################
# 3)


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# def minServiceCenters(root):
#     centers = 0

#     print("Program started")
#     def dfs(node):
#         nonlocal centers

#         # Null node is already covered
#         if not node:
#             return 2

#         left = dfs(node.left)
#         right = dfs(node.right)

#         # If any child needs service → place center here
#         if left == 0 or right == 0:
#             centers += 1
#             return 1

#         # If any child has a center → this node is covered
#         if left == 1 or right == 1:
#             return 2

#         # Otherwise → this node needs service
#         return 0

#     # If root still needs service, add one center
#     if dfs(root) == 0:
#         centers += 1

#     return centers






# # Input = {0, 0, null, 0, null, 0, null, null, 0}

# root = TreeNode(0)
# root.left = TreeNode(0)
# root.left.left = TreeNode(0)
# root.left.left.left = TreeNode(0)
# root.left.left.left.right = TreeNode(0)

# print(minServiceCenters(root))



# 🔹 Problem Explained in Easy Words

# Each city = one tree node

# A service center placed at a node can serve:

# that node itself

# its parent

# its immediate children

# 👉 Goal: Place the minimum number of service centers so every city is covered.




# 🔹 Key Insight (Very Important)

# Instead of deciding where to place centers, we decide the state of each node.

# Each node can be in one of 3 states:

# State	Meaning
# 0	This node needs service
# 1	This node has a service center
# 2	This node is already covered



# Strategy (Greedy + DFS)

# We traverse the tree from bottom to top (postorder):

# If any child needs service (0)
# → place a service center at the current node

# If any child has a service center (1)
# → current node is covered

# Otherwise
# → current node needs service

# At the end:

# If the root still needs service, place one more center.












################################################################################################################
#4. 
















################################################################################################################
#5 a

# Advanced Algorithm Design with GUI Integration
# Project Title: Interactive Emergency Network Simulator

################################################################################################################
#5b

#Multithreaded Sorting Application

# 🔍 What the question is asking (in simple words)

# You are asked to build a multithreaded sorting program with 3 threads:

# 1️⃣ Main (parent) thread

#     Holds a global array of integers (unsorted).

#     Splits the array into two equal halves.

#     Creates:

#         Thread 1 → sorts the first half

#         Thread 2 → sorts the second half

#     Waits for both sorting threads to finish.

#     Starts Thread 3 (merging thread).

#     Finally prints the fully sorted array.

# 2️⃣ Sorting threads (2 threads)

#     Each thread:

#         Receives a starting index and ending index.

#         Sorts only its portion of the global array.

#     Any sorting algorithm is allowed (bubble sort, quicksort, etc.).

# 3️⃣ Merging thread (1 thread)

#     Takes the two already sorted halves.

#     Merges them into a second global array.

#     This is similar to the merge step of merge sort.

# 🧠 Key concepts being tested

#     Multithreading

#     Shared global data

#     Passing parameters to threads

#     Thread synchronization (join)

#     Divide-and-conquer idea









# import threading

# # ---------- Global data ----------
# arr = [38, 27, 43, 3, 9, 82, 10, 5]
# n = len(arr)

# # Second global array for merged result
# merged_arr = [0] * n


# # ---------- Sorting function ----------
# def sort_sublist(start, end):
#     """
#     Sorts a portion of the global array arr
#     from index 'start' to 'end' (inclusive)
#     """
#     # Simple bubble sort (easy to understand)
#     for i in range(start, end + 1):
#         for j in range(start, end):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]


# # ---------- Merging function ----------
# def merge_sublists(mid):
#     """
#     Merges two sorted halves of arr into merged_arr
#     """
#     i = 0        # pointer for left half
#     j = mid + 1 # pointer for right half
#     k = 0        # pointer for merged_arr

#     # Merge while both halves have elements
#     while i <= mid and j < n:
#         if arr[i] <= arr[j]:
#             merged_arr[k] = arr[i]
#             i += 1
#         else:
#             merged_arr[k] = arr[j]
#             j += 1
#         k += 1

#     # Copy remaining elements from left half
#     while i <= mid:
#         merged_arr[k] = arr[i]
#         i += 1
#         k += 1

#     # Copy remaining elements from right half
#     while j < n:
#         merged_arr[k] = arr[j]
#         j += 1
#         k += 1


# # ---------- Main (Parent Thread) ----------
# if __name__ == "__main__":
#     print("Original array:", arr)

#     mid = n // 2 - 1

#     # Create sorting threads
#     t1 = threading.Thread(target=sort_sublist, args=(0, mid))
#     t2 = threading.Thread(target=sort_sublist, args=(mid + 1, n - 1))

#     # Start sorting threads
#     t1.start()
#     t2.start()

#     # Wait for both sorting threads to finish
#     t1.join()
#     t2.join()

#     print("After sorting sublists:", arr)

    

#     # Create and start merging thread
#     t3 = threading.Thread(target=merge_sublists, args=(mid,))
#     t3.start()
#     t3.join()

#     print("Final sorted array:", merged_arr)








# “We divide the array into two halves and sort each half using two separate threads. Since threads share global memory, 
# both threads directly modify the same array but in different index ranges. After both sorting threads finish, 
# a third thread merges the two sorted halves into another global array. The parent thread waits for all threads using join() 
# and then prints the final sorted result.”



# but after sorted sublists are in same array in ouput, it should have been in 2 different arrays, right?

# Yes, logically:

# There are two different sublists

# Each sorting thread should work on its own list

# but we here work on 1 array don't make multiple left or right arrays, so
#Physically one array, logically two sublists.


################################################################################################################
#6


graph = {
    "Glogow": ["Leszno", "Wroclaw"],
    "Leszno": ["Glogow", "Poznan", "Kalisz", "Wroclaw"],
    "Wroclaw": ["Leszno", "Opole"],
    "Opole": ["Wroclaw", "Katowice"],
    "Katowice": ["Opole", "Czestochowa", "Krakow"],
    "Czestochowa": ["Katowice", "Lodz"],
    "Kalisz": ["Leszno", "Poznan", "Lodz"],
    "Poznan": ["Leszno", "Kalisz", "Bydgoszcz"],
    "Bydgoszcz": ["Poznan", "Wloclawek", "Konin"],
    "Konin": ["Bydgoszcz", "Lodz"],
    "Wloclawek": ["Bydgoszcz", "Plock"],
    "Lodz": ["Konin", "Kalisz", "Czestochowa", "Warsaw"],
    "Warsaw": ["Lodz", "Plock", "Radom"],
    "Radom": ["Warsaw", "Kielce"],
    "Kielce": ["Radom", "Krakow"],
    "Krakow": ["Katowice", "Kielce"],
    "Plock": ["Wloclawek", "Warsaw"]
}


#1 a Depth First Search (DFS)

# DFS Idea (Human Explanation)
# Go as deep as possible before backtracking
# Uses a stack
# Does not guarantee shortest path
# Can get stuck exploring long paths first


# OPEN Container (Frontier)

# OPEN = nodes that are discovered but not yet explored
# These are cities the robot knows about
# But hasn’t visited yet
# Different algorithms manage OPEN differently
# Example:
# OPEN = [Glogow, Leszno, Wroclaw]
# Meaning:
# ➡ The robot can go to these cities next


# CLOSED Container (Explored Set)
# CLOSED = nodes that are already explored
# These cities have already been visited
# They will NOT be visited again
# Prevents infinite loops
# Example:
# CLOSED = [Glogow, Leszno]
# Meaning:
# ➡ The robot has already explored these cities


# Why do we need OPEN and CLOSED?

# ✔ Avoid revisiting the same city
# ✔ Track progress of the algorithm
# ✔ Clearly explain algorithm steps (important for marks)
# ✔ Prevent infinite loops in graphs


# def dfs(graph, start, goal):
#     open_stack = [start]
#     closed = []
#     parent = {}

#     while open_stack:
#         current = open_stack.pop()
#         closed.append(current)

#         if current == goal:
#             break

#         for neighbor in graph[current]:
#             if neighbor not in open_stack and neighbor not in closed:
#                 parent[neighbor] = current
#                 open_stack.append(neighbor)

#     # Reconstruct path
#     path = []
#     node = goal
#     while node != start:
#         path.append(node)
#         node = parent[node]
#     path.append(start)

#     print("Path closed")
#     return path[::-1], closed

# start = "Glogow"
# goal = "Plock"

# finalPath, closedContainer = dfs(graph, start, goal)
# print("Path:",finalPath)
# print("Closed Container:", closedContainer)



#
# Final Path vs CLOSED Container (Simple Explanation)
# They are NOT the same thing, even though sometimes they look similar.

# The final path is:
# The actual route the robot will follow from the start city to the goal city.


# Key points

# Starts at Glogow
# Ends at Plock
# Must follow valid connections
# This is the answer to the problem


#Why it matters

# ✔ Used for navigation
# ✔ Used to calculate cost
# ✔ What the robot actually does


# CLOSED Container
# The CLOSED container is:
# A list of all cities that were explored during the search process.

# Key points

# Includes every visited city
# Order shows search behavior
# May contain cities not in final path




# DFS Execution (Example)

# OPEN: [Glogow]
# CLOSED: []

# Visit Glogow → go to Leszno
# Leszno → Poznan
# Poznan → Bydgoszcz
# Bydgoszcz → Wloclawek
# Wloclawek → Plock (Goal)




################################################################################################################
# 6)1)b) Breadth First Search



graph = {
    "Glogow": ["Leszno", "Wroclaw"],
    "Leszno": ["Glogow", "Poznan", "Kalisz", "Wroclaw"],
    "Wroclaw": ["Leszno", "Opole"],
    "Opole": ["Wroclaw", "Katowice"],
    "Katowice": ["Opole", "Czestochowa", "Krakow"],
    "Czestochowa": ["Katowice", "Lodz"],
    "Kalisz": ["Leszno", "Poznan", "Lodz"],
    "Poznan": ["Leszno", "Kalisz", "Bydgoszcz"],
    "Bydgoszcz": ["Poznan", "Wloclawek", "Konin"],
    "Konin": ["Bydgoszcz", "Lodz"],
    "Wloclawek": ["Bydgoszcz", "Plock"],
    "Lodz": ["Konin", "Kalisz", "Czestochowa", "Warsaw"],
    "Warsaw": ["Lodz", "Plock", "Radom"],
    "Radom": ["Warsaw", "Kielce"],
    "Kielce": ["Radom", "Krakow"],
    "Krakow": ["Katowice", "Kielce"],
    "Plock": ["Wloclawek", "Warsaw"]
}



# BFS Idea (Human Explanation)
# Explores level by level
# Uses a queue
# Always finds the shortest path (in number of steps)
# Memory expensive

# from collections import deque

# def bfs(graph, start, goal):
#     open_queue = deque([start])
#     closed = []
#     parent = {}

#     while open_queue:
#         current = open_queue.popleft()
#         closed.append(current)

#         if current == goal:
#             break

#         for neighbor in graph[current]:
#             if neighbor not in open_queue and neighbor not in closed:
#                 parent[neighbor] = current
#                 open_queue.append(neighbor)

#     # Reconstruct path
#     path = []
#     node = goal
#     while node != start:
#         path.append(node)
#         node = parent[node]
#     path.append(start)

#     return path[::-1], closed

# start = "Glogow"
# goal = "Plock"


# finalPath, closedContainer = bfs(graph, start, goal)
# print("Path:",finalPath)
# print("Closed Container:", closedContainer)



# BFS Result
# ✔ Shortest path in terms of number of cities

################################################################################################################
# 2) Heuristic Design & A* Algorithm
# Now using diagram b
# What is the heuristic function in A*?

# In A*, the heuristic is a function, usually written as: h(n)
# Diagram (b) provides straight-line distances to Plock.

# The heuristic function h(n) estimates the cost from the current node n to the goal node.

# This is a valid heuristic because:
#     It never overestimates the actual distance
#     It is admissible and consistent


heuristic = {
    "Glogow": 40,
    "Leszno": 67,
    "Poznan": 108,
    "Bydgoszcz": 90,
    "Wloclawek": 44,
    "Konin": 102,
    "Kalisz": 95,
    "Lodz": 118,
    "Warsaw": 95,
    "Plock": 0
}

# A* Evaluation Function f(n) = g(n) + h(n)

# Where:

    # g(n) = cost from start
    # h(n) = heuristic estimate to goal

# A* Algorithm Implementation

# import heapq

# def a_star(graph, heuristic, start, goal):
#     open_list = []
#     heapq.heappush(open_list, (0, start))
#     parent = {}
#     g_cost = {start: 0}
#     closed = []

#     while open_list:
#         _, current = heapq.heappop(open_list)
#         closed.append(current)

#         if current == goal:
#             break

#         for neighbor in graph[current]:
#             temp_g = g_cost[current] + 1  # simplified step cost

#             if neighbor not in g_cost or temp_g < g_cost[neighbor]:
#                 g_cost[neighbor] = temp_g
#                 f = temp_g + heuristic.get(neighbor, 0)
#                 heapq.heappush(open_list, (f, neighbor))
#                 parent[neighbor] = current

#     # Reconstruct path
#     path = []
#     node = goal
#     while node != start:
#         path.append(node)
#         node = parent[node]
#     path.append(start)

#     return path[::-1], closed



# start = "Glogow"
# goal = "Plock"



# finalPath, closedContainer = a_star(graph, heuristic, start, goal)
# print("Path:",finalPath)
# print("Closed Container:", closedContainer)





# A* Result

# Optimal Path Found Faster:

# ✔ Optimal
# ✔ Efficient
# ✔ Goal-directed

################################################################################################################
# 3. Comparison: DFS vs BFS vs A*


# In This Problem:

#     DFS found a solution but without optimality guarantee
#     BFS found shortest path but explored many nodes
#     A* found the best path faster, using straight-line distances

# Algorithm	            Advantages	                                Disadvantages
# DFS	                Low memory usage, simple	                Not optimal, may take long path
# BFS	                Guaranteed shortest path	                High memory usage
# A*	                Optimal + efficient, goal-directed	        Needs good heuristic





# Final Conclusion

# For the parcel delivery robot:

    # DFS is not reliable
    # BFS is correct but inefficient
    # A* is the best choice, as it uses geographical knowledge (diagram b)




# Discussion: BFS, DFS and A* in the Parcel Delivery Problem

# In this problem, a robot is required to deliver parcels from Glogow (start city) to Plock (goal city) using a map of Polish cities. Different search algorithms were applied to find a route, and each algorithm showed distinct strengths and weaknesses based on how it explores the state space.

# 1. Depth First Search (DFS)

# DFS explores one path deeply before backtracking.
# In our problem, DFS started from Glogow and followed one branch of cities until it eventually reached Plock.

# Advantages (in this context)

# DFS uses less memory because it only stores the current path and a small number of unexplored nodes.

# It was able to find a valid path from Glogow to Plock without needing additional information such as distances or heuristics.

# Simple to implement and easy to understand.

# Disadvantages (in this context)

# DFS does not guarantee the shortest path. The path it found may contain unnecessary detours.

# The algorithm may explore irrelevant cities before reaching Plock.

# In larger maps, DFS can waste time by going deep into poor routes.

# 🔎 Observation from our result:
# DFS found a solution, but there was no guarantee that the route was optimal for parcel delivery.

# 2. Breadth First Search (BFS)

# BFS explores all cities level by level, starting from the nearest cities to Glogow.

# Advantages (in this context)

# BFS guarantees the shortest path in terms of number of cities visited.

# It is reliable and systematic, ensuring that Plock is reached using the minimum number of steps.

# Useful when all actions have equal cost.

# Disadvantages (in this context)

# BFS requires large memory, as it stores all frontier nodes at each level.

# It does not consider actual road distances, only the number of edges.

# Many cities were explored even when they were not part of the final path.

# 🔎 Observation from our result:
# BFS produced a correct and shortest-step route, but it explored many unnecessary cities, making it inefficient for large maps.

# 3. A* Search Algorithm

# A* combines actual path cost and heuristic information to guide the search toward the goal.

# In this problem, the heuristic was the straight-line distance to Plock (from diagram b).

# Advantages (in this context)

# A* found the optimal path efficiently.

# It explored fewer cities compared to BFS because it was guided by geographical information.

# The algorithm is both complete and optimal when the heuristic is admissible.

# Very suitable for real-world navigation problems like parcel delivery.

# Disadvantages (in this context)

# Requires a well-designed heuristic, which may not always be available.

# More complex to implement than BFS and DFS.

# Slightly higher memory usage than DFS.

# 🔎 Observation from our result:
# A* reached Plock faster and more efficiently than BFS and DFS by prioritizing cities closer to the goal.










################################################################################################################


################################################################################################################





################################################################################################################


################################################################################################################


################################################################################################################


################################################################################################################


################################################################################################################

