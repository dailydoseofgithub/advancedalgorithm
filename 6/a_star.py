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


# The heuristic values generated from diagram (b)

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
    "Radom": 91,
    "Krakow":102,
    "Plock": 0
    
}





# A* Evaluation Function f(n) = g(n) + h(n)

# Where:

    # g(n) = cost from start
    # h(n) = heuristic estimate to goal




# A* Algorithm Implementation


import heapq

def a_star(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    parent = {}
    g_cost = {start: 0}
    closed = []

    while open_list:
        _, current = heapq.heappop(open_list)
        closed.append(current)

        if current == goal:
            break

        for neighbor in graph[current]:
            temp_g = g_cost[current] + 1  # simplified step cost

            if neighbor not in g_cost or temp_g < g_cost[neighbor]:
                g_cost[neighbor] = temp_g
                f = temp_g + heuristic.get(neighbor, 0)
                heapq.heappush(open_list, (f, neighbor))
                parent[neighbor] = current

    # Reconstruct path
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent[node]
    path.append(start)

    return path[::-1], closed



start = "Glogow"
goal = "Plock"



finalPath, closedContainer = a_star(graph, heuristic, start, goal)
print("Path:",finalPath)
print("Closed Container:", closedContainer)
