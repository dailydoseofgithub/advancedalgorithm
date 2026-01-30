# TASK 1: Modelling the input data

# I am making use of python dictionaries
# Hourly Energy Demand (kWh)

demand = {
    6: {"A": 20, "B": 15, "C": 25},
    7: {"A": 22, "B": 16, "C": 28},
    18: {"A": 30, "B": 25, "C": 35},   # higher demand hour
}

# Source of energy information
sources = [
    {"id": "S1", "type": "Solar",  "capacity": 50, "start": 6,  "end": 18, "cost": 1.0},
    {"id": "S2", "type": "Hydro",  "capacity": 40, "start": 0,  "end": 24, "cost": 1.5},
    {"id": "S3", "type": "Diesel", "capacity": 60, "start": 17, "end": 23, "cost": 3.0},
]


# TASK 4: Handlling ±10% demand flexibility


def within_tolerance(actual, required):
    """
    Checks whether the supplied energy is within ±10% of demand
    """
    return 0.9 * required <= actual <= 1.1 * required



# TASK 2 & 3: Hourly allocation using DP concepts + Greedy strategy



results = {}          #  Resuls stores hourly allocation details
total_cost = 0        # Total system cost
renewable_energy = 0  # Solar + Hydro energy
diesel_energy = 0     # Diesel energy

for hour, districts in demand.items():

    print(f"\nHour {hour}: Allocation")

    # This is remaining demand per district
    remaining_demand = districts.copy()

    # Filtering the available sources for this hour
    available_sources = [
        s for s in sources if s["start"] <= hour < s["end"]
    ]

    # GREEDY: Sort sources by lowest cost first

    # Greedy Rule
    # We always use the cheapest available energy source first
    # The order of preference should be:
    # Solar (Rs. 1.0)
    # Hydro (Rs. 1.5)
    # Diesel (Rs. 3.0)


    available_sources.sort(key=lambda s: s["cost"])

    hour_allocation = {}

    # We can see Dynamic Programming idea:
    
    # At each step we have to decide how much to take from a source
    # while tracking remaining demand and capacity

    for source in available_sources:
        source_type = source["type"]
        capacity_left = source["capacity"]
        hour_allocation[source_type] = {}

        for district in remaining_demand:
            if capacity_left <= 0:
                break

            needed = remaining_demand[district]

            if needed > 0:
                supplied = min(needed, capacity_left)
                hour_allocation[source_type][district] = supplied
                remaining_demand[district] -= supplied
                capacity_left -= supplied

                # Calculating the cost
                cost = supplied * source["cost"]
                total_cost += cost

                # Renewable vs Diesel tracking
                if source_type in ["Solar", "Hydro"]:
                    renewable_energy += supplied
                else:
                    diesel_energy += supplied

    # We are going to save hourly results here
    results[hour] = hour_allocation


# TASK 5: Output table of results

print("\nFinal Allocation Table\n")

for hour, allocation in results.items():
    print(f"Hour {hour}")
    for source, dist_data in allocation.items():
        for d, val in dist_data.items():
            print(f"  {source} -> District {d}: {val} kWh")
    print()



# TASK 6: Cost & resource usage analysis


total_energy = renewable_energy + diesel_energy
renewable_percent = (renewable_energy / total_energy) * 100 if total_energy else 0

print("ANALYSIS REPORT")
print(f"Total Cost of Distribution: Rs. {total_cost:.2f}")
print(f"Renewable Energy Usage: {renewable_percent:.2f}%")
print(f"Diesel Energy Used: {diesel_energy} kWh")

print("\nDiesel Usage Explanation:")
print("- Diesel is used only during evening hours (17–23)")
print("- Solar is unavailable, and hydro capacity alone is insufficient")
print("- Greedy strategy delays diesel usage as long as possible")


print("\nAlgorithm Efficiency & Trade-offs:")
print("- Time Complexity: O(H × S × D)")
print("- Greedy ensures low cost but may miss global optimum")
print("- Dynamic tracking of demand makes it suitable for real-time grids")




















