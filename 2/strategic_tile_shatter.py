def max_points(tile_multipliers):
    n = len(tile_multipliers) #Number of tiles
    nums = [1] + tile_multipliers + [1]
 


    dp = [[0] * (n + 2) for _ in range(n + 2)]



    for length in range(1, n + 1): 
        for left in range(1, n - length + 2):
            right = left + length - 1
 
            for i in range(left, right + 1):
                dp[left][right] = max(
                    dp[left][right],  
                    dp[left][i-1] + dp[i+1][right] + nums[left-1] * nums[i] * nums[right+1]
                )

    # The maximum points for the full array is stored in dp[1][n]
    return dp[1][n]


# Example 
print(max_points([3, 1, 5, 8]))









# In this problem, we have a row of tiles, each with a number (score multiplier):
# Example: [3, 1, 5, 8]

# You shatter tiles one by one.
# When you shatter a tile, you get points equal to:

    # left neighbor × tile itself × right neighbor

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

# That’s the maximum points we can get.

