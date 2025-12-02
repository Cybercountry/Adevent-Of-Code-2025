# Read input from file
data = []
with open("input.txt") as f:
    data = [row.strip() for row in f if row.strip()]

# Variables
dial_position = 50
zero_hits = 0
zero_crossings = 0

# Process commands
for item in data:
    dial_direction = item[0]
    magnitude = int(item[1:])

    # Check whether the first 't' pass through 0 occurs at each rotation
    if dial_direction == "R":
        # Form: t = (100 - x) % 100
        t = (100 - dial_position) % 100
        # Special case: if t = 0, so the real first pass is at t = 100
        if t == 0:
            t = 100
    else:
        # Form: t = x
        t = dial_position
        # Same situation where the dial starts at 0, in this case t = 100
        if t == 0:
            t = 100

    # Check the first pass happens within the rotation range [0, magnitude)
    if t < magnitude:
        # 1 occurrence or more
        zero_crossings += 1

        # Calculate the maximum number of occurrences within the magnitude
        k_max = (magnitude - 1 - t) // 100
        zero_crossings += k_max

    # Update the dial position applying the direction
    if dial_direction == "R":
        dial_position = (dial_position + magnitude) % 100
    else:  # 'L'
        dial_position = (dial_position - magnitude) % 100

    # Count if the rotation ends exactly at 0
    if dial_position == 0:
        zero_hits += 1

print(zero_hits + zero_crossings)
