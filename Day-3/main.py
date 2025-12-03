def greedy_stack(n, k):
    remove = len(n) - k
    stack = []

    for i in n:
        while remove > 0 and stack and stack[-1] < i:
            stack.pop()
            remove -= 1
        stack.append(i)

    # In special cases, like decreasing numbers,
    # we need to ensure we remove enough elements
    if remove > 0:
        stack = stack[:-remove]

    return int("".join(stack))


# Read input from the txt
with open("input.txt", "r") as file:
    data = file.read().strip().split("\n")

# exemple = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]

# Variables
total = 0
k = 12

# Main loop
for num in data:
    total += greedy_stack(num, k)  # O(n)

print(total)
