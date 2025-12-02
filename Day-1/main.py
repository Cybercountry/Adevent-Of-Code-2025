# Read input from file
data = []
with open("input.txt") as f:
    data = [row.strip() for row in f if row.strip()]

# Variables
dial_position = 50
zero_hits = 0

# Process commands
for item in data:
    spin_direction = item[0]
    value = int(item[1:])

    # According to the problem statement,
    # if we encounter the letter 'R',
    # it indicates we should perform an addition operation by turning the dial to the right.
    if spin_direction == "R":
        dial_position = (dial_position + value) % 100
    # If it’s not the letter R, then it will be the letter 'L', and in this case,
    # we do the opposite—a subtraction by turning the dial to the left.
    else:
        dial_position = (dial_position - value) % 100
    # The problem states that numbers range from 0 to 99,
    # so we need to handle circular counting, which we can achieve using modulo,
    # 100 in this case, since that’s the total number of elements we have.

    # Count how many times the dial returns to 0
    if dial_position == 0:
        zero_hits += 1

print(zero_hits)
