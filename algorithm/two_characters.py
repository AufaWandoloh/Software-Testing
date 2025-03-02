def alternate(s):
    unique_chars = set(s)
    max_length = 0

    for char1 in unique_chars:
        for char2 in unique_chars:
            if char1 != char2:
                filtered_string = [c for c in s if c == char1 or c == char2]
                if all(
                    filtered_string[i] != filtered_string[i - 1]
                    for i in range(1, len(filtered_string))
                ):
                    max_length = max(max_length, len(filtered_string))

    return max_length
