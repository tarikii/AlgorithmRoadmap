def containsDuplicate(nums: list[int]) -> bool:
    hash_set = set()

    for n in nums:

        if n in hash_set:
            return True

        hash_set.add(n)

    return False


def main():
    nums = [1, 2, 3, 4, 5, 7, 8, 7]

    print(containsDuplicate(nums))


if __name__ == "__main__":
    main()
