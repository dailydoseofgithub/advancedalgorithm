# This is the list of the cities that was given in the diagram

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

def dfs(graph, start, goal):
    open_stack = [start]
    closed = []
    parent = {}

    while open_stack:
        current = open_stack.pop()
        closed.append(current)

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in open_stack and neighbor not in closed:
                parent[neighbor] = current
                open_stack.append(neighbor)

    # Reconstructing path
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent[node]
    path.append(start)

    print("Path closed")
    return path[::-1], closed

start = "Glogow"
goal = "Plock"

finalPath, closedContainer = dfs(graph, start, goal)
print("Path:",finalPath)
print("Closed Container:", closedContainer)


