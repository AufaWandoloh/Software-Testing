def caesarCipher(s, k):
    k = k % 26
    result = []

    for c in s:
        if "a" <= c <= "z":
            new_char = chr((ord(c) - ord("a") + k) % 26 + ord("a"))
            result.append(new_char)
        elif "A" <= c <= "Z":
            new_char = chr((ord(c) - ord("A") + k) % 26 + ord("A"))
            result.append(new_char)
        else:
            result.append(c)

    return "".join(result)
