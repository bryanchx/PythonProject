def sort(nums):
    length = len(nums)
    count = 0
    for i in range(1, length):
        for j in range(i, -1, -1):
            if j >= 1:
                if nums[j] < nums[j - 1]:
                    print(nums)
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
                else:
                    break
            count += 1
        # print(nums)
    print(f'一共运行了{count}次')


if __name__ == '__main__':
    nums = [19, 5, 32, 4, 9, 5, 75, 42, 12, 4, 2, 9]
    sort(nums)
