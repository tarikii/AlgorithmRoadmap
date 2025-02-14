from collections import Counter

def topKFrequent(nums: list[int], k: int) -> list[int]:
    repeated_numbers = Counter(nums)

    res = [num for num, freq in repeated_numbers.most_common(k)]

    return sorted(res)

def main():
    nums = [1, 2, 2, 3, 3, 3]
    k = 2

    print(topKFrequent(nums, k))


if __name__ == "__main__":
    main()
