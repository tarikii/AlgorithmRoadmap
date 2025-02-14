def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(str):
    res = []
    i = 0

    while i < len(str):
        j = i
        while str[j] != "#":
            j += 1
        length = int(str[i:j])
        res.append(str[j + 1 : j + 1 + length])
        i = j + 1 + length
    return res

def main():
    # Test cases
    test_cases = [
        ["hello", "world"],
        ["", "a", "abc", "12345"],
        ["special#chars", "test#case", "#"],
        ["longer string with spaces", "another one"],
    ]

    for i, test in enumerate(test_cases):
        encoded = encode(test)
        decoded = decode(encoded)
        print(f"Test Case {i+1}:")
        print(f"Original: {test}")
        print(f"Encoded: {encoded}")
        print(f"Decoded: {decoded}")
        print(f"Pass: {test == decoded}\n")

if __name__ == "__main__":
    main()
