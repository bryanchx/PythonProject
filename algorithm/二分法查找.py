def binary_search(nums, num, l, r):
    if l <= r:
        mid = (l + r) // 2
        if nums[mid] == num:
            return mid
        elif nums[mid] < num:
            return binary_search(nums, num, mid + 1, r)
        elif nums[mid] > num:
            return binary_search(nums, num, l, mid - 1)
    return -1


def binary_search2(nums, num, l, r):
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == num:
            return mid
        elif nums[mid] < num:
            l = mid + 1
        elif nums[mid] > num:
            r = mid - 1
    return -1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l = sorted(nums, reverse=False)
    # search = binary_search(l, 10, 0, len(l) - 1)
    search = binary_search2(l, 5, 0, len(l) - 1)
    print(search)
