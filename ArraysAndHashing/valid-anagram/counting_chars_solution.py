def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    countS = {}
    countT = {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)


    for c in countS:
        if countS[c] != countT.get(c):
            return False

    return True

def main():

    s = "racecar"
    t = "carrace"

    s2 = "jar"
    t2 = "jam"

    print(str(isAnagram(s, t)) + "\n")
    print(str(isAnagram(s2, t2)) + "\n")

if __name__ == "__main__":
    main()
