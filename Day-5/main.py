def read_ranges(filename="input.txt"):
    ranges = []
    with open(filename) as file:
        for row in file:
            row = row.strip()

            if row == "":
                break

            start, end = map(int, row.split("-"))
            ranges.append((int(start), int(end)))

    return ranges


# O(n log n)
# Memory: O(n)
def main():
    # Sorted Example = [(10, 14), (11, 20)]
    sorted_ranges = sorted(read_ranges(), key=lambda x: x[0])

    total = 0
    current_start, current_end = sorted_ranges[0]

    """
    The overlap condition: start <= current_end + 1
    [10, 14]
    start, end = [11, 20] -> 11 <= 14+1 (15) -> True
    Ranges:     [10---14]
                      [11---------20]
    Result:
    [10------------------20]
    """

    for start, end in sorted_ranges[1:]:
        if start <= current_end + 1:
            # Overlap or adjacent -> merge, extend current range
            current_end = max(current_end, end)
        else:
            # If no overlap, sum the finished range and reset current range
            total += current_end - current_start + 1
            current_start, current_end = start, end

    # Add the last range to the total
    total += current_end - current_start + 1
    print(total)


if __name__ == "__main__":
    main()
