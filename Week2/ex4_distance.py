def calculate_levenshtein_distance(source, target):
    m, n = len(source), len(target)

    if m == 0:
        return n
    if n == 0:
        return m

    # Initialize the previous and current rows
    prev_row = list(range(n + 1))
    current_row = [0] * (n + 1)

    for i in range(1, m + 1):
        current_row[0] = i
        for j in range(1, n + 1):
            sub_cost = 0 if source[i - 1] == target[j - 1] else 1
            current_row[j] = min(
                prev_row[j] + 1,          # Deletion
                current_row[j - 1] + 1,   # Insertion
                prev_row[j - 1] + sub_cost  # Substitution
            )
        prev_row, current_row = current_row, prev_row

    return prev_row[n]


# Test cases
assert calculate_levenshtein_distance("kitten", "sitting") == 3
assert calculate_levenshtein_distance("yu", "you") == 1


if __name__ == "__main__":
    str_source = "yu"
    str_target = "you"
    print(f"Levenshtein distance between {str_source} and {str_target} is",
          calculate_levenshtein_distance(str_source, str_target))
