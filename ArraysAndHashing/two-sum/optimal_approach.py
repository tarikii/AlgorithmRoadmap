def twoSum(nums: list[int], target: int) -> list[int]:
    hash_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in hash_map and hash_map[complement] != i:
            return [hash_map[complement], i]
        
        hash_map[num] = i

    return []

def main():
    nums = [3, 4, 5, 6]
    target = 7

    print(twoSum(nums, target))


if __name__ == "__main__":
    main()
