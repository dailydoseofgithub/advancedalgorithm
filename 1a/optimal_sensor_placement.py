import math

def geometric_median(sensor_locations, eps=1e-6, max_iter=1000):
    
    # Here, first of all we are going to initialize at centroid


    x = sum(p[0] for p in sensor_locations) / len(sensor_locations)
    y = sum(p[1] for p in sensor_locations) / len(sensor_locations)

    for _ in range(max_iter):
        num_x = 0.0
        num_y = 0.0
        weight_sum = 0.0

        for xi, yi in sensor_locations:
            dist = math.hypot(x - xi, y - yi)

            # If those hub coincides with a sensor, it is optimal
            if dist < eps:
                return xi, yi

            weight = 1.0 / dist
            num_x += xi * weight
            num_y += yi * weight
            weight_sum += weight

        new_x = num_x / weight_sum
        new_y = num_y / weight_sum

        # Check convergence
        if math.hypot(new_x - x, new_y - y) < eps:
            break

        x, y = new_x, new_y

    return x, y


def total_distance(hub_x, hub_y, sensor_locations):

    return sum(math.hypot(hub_x - xi, hub_y - yi) for xi, yi in sensor_locations)



sensors = [
    (0,1),(1,0),(1,2),(2,1)
]

hub_x, hub_y = geometric_median(sensors)
distance_sum = total_distance(hub_x, hub_y, sensors)

print("Optimal hub location:", (hub_x, hub_y))
print("Minimum total distance:", distance_sum)




# In this approach, it minimizes sum of Euclidean distances, not squared distances
# The centroid is not optimal for this problem
