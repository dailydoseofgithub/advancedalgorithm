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



from collections import deque

def bfs(graph, start, goal):
    open_queue = deque([start])
    closed = []
    parent = {}

    while open_queue:
        current = open_queue.popleft()
        closed.append(current)

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in open_queue and neighbor not in closed:
                parent[neighbor] = current
                open_queue.append(neighbor)

    # Reconstructing path
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent[node]
    path.append(start)

    return path[::-1], closed

start = "Glogow"
goal = "Plock"


finalPath, closedContainer = bfs(graph, start, goal)
print("Path:",finalPath)
print("Closed Container:", closedContainer)
