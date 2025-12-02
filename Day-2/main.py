"""
To identify an invalid ID, it is necessary to check if:
    - It has a pattern that repeats at least 2 times or more.
"""


def is_invalid_id(n):
    s = str(n)

    # For an n-digit number, it's necessary to test all pattern sizes k
    # where k divides n.
    # Form: (k % n == 0)
    for size in range(1, len(s) // 2 + 1):
        block = s[:size]
        if len(s) % size == 0 and block * (len(s) // size) == s:
            return True

    return False


def main():
    data = input()

    total = 0
    ranges = data.split(",")

    for r in ranges:
        r = r.strip()
        if not r:
            continue

        start_id, end_id = map(int, r.split("-"))

        # end_id + 1 to ensure it iterates over all numbers in the range
        for n in range(start_id, end_id + 1):
            if is_invalid_id(n):
                total += n

    print(total)


if __name__ == "__main__":
    main()
