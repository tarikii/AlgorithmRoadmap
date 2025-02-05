from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26 # 26 characters in the alphabet a...z

        for c in s:
            count[ord(c) - ord('a')] += 1

        res[tuple(count)].append(s)


    sorted_res = sorted([sorted(group) for group in res.values()], 
            key=lambda x: (len(x) > 1, x))
    return sorted_res

def main():
    strs = ["act","pots","tops","cat","stop","hat"]

    print(groupAnagrams(strs))


if __name__ == "__main__":
    main()
