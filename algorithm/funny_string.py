def funnyString(s):
    n = len(s)
    ascii_values = [ord(c) for c in s]
    rev_ascii_values = ascii_values[::-1]

    for i in range(1, n):
        if abs(ascii_values[i] - ascii_values[i - 1]) != abs(
            rev_ascii_values[i] - rev_ascii_values[i - 1]
        ):
            return "Not Funny"

    return "Funny"
