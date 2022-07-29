def sort(nums):
    length = len(nums)
    count = 0
    for i in range(length):
        for j in range(i, length - 1):
            count += 1
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    print(nums)
    print(f'一共运行了{count}次')


if __name__ == '__main__':
    nums = [19, 5, 32, 4, 9, 5, 75, 42, 12, 4, 2, 9]
    sort(nums)
