def sort(nums):
    length = len(nums)
    count = 0
    for i in range(length):
        minIndex = i
        for j in range(i + 1, length):
            count += 1
            if nums[minIndex] > nums[j]:
                minIndex = j

        if nums[i] > nums[minIndex]:
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
        print(nums)

    print(nums)
    print(f'一共运行了{count}次')


if __name__ == '__main__':
    nums = [19, 5, 32, 4, 9, 5, 75, 42, 12, 4, 2, 9]
    sort(nums)
