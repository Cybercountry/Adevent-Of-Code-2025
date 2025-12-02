"""
To find a Invalid ID, It's necessary to check 3 things:
    1- It has an even number of digits;
    2- It's possible split the number in half;
    3- The first half is equal to the second half;
"""


def is_invalid_id(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False  # Only numbers with an even number of digits can be invalid IDs.

    half = len(s) // 2
    return s[:half] == s[half:]


def main():
    data = input()

    total = 0
    ranges = data.split(",")

    for r in ranges:
        r = r.strip()
        if not r:
            continue

        start_id, end_id = map(int, r.split("-"))

        for n in range(start_id, end_id + 1):
            if is_invalid_id(n):
                total += n

    print(total)


if __name__ == "__main__":
    main()
