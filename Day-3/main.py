# Read input from the txt
with open("input.txt", "r") as file:
    data = file.read().strip().split("\n")

"""
exemples = [
    "987654321111111",  # 98
    "811111111111119",  # 89
    "234234234234278",  # 78
    "818181911112111",  # 92
    # Sum = 357
]
"""

total = 0

for num in data:
    best_combination = -1

    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            value = int(num[i] + num[j])
            if value > best_combination:
                best_combination = value

    total += best_combination

print(total)
