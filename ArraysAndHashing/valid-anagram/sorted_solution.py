def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def main():
    s = "racecar"
    t = "carrace"

    s2 = "jar"
    t2 = "jam"

    print(str(isAnagram(s, t)) + "\n")
    print(str(isAnagram(s2, t2)) + "\n")


if __name__ == "__main__":
    main()
