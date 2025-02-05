def containsDuplicate(nums: list[int]) -> bool:
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):

            if nums[i] == nums[j]:
                return True


    return False



def main():
    nums = [1, 2, 3, 6, 6]

    print(containsDuplicate(nums))


if __name__ == '__main__':
    main()
