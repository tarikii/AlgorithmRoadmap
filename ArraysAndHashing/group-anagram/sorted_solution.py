def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = []
    seen = set()

    for i in range(len(strs)):
        
        if strs[i] in seen:
            continue

        anagrams = [strs[i]]
        for j in range(i + 1, len(strs)):

            if sorted(strs[i]) == sorted(strs[j]):
                anagrams.append(strs[j])
                seen.add(strs[j])

        result.append(sorted(anagrams))

    result.sort(key=lambda x: (len(x) > 1, x))

    return result

def main():
    strs = ["act","pots","tops","cat","stop","hat"]

    print(groupAnagrams(strs))


if __name__ == "__main__":
    main()
