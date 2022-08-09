def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    key = nums[0]
    pList, list, aList = [], [], []
    for i in range(len(nums)):
        if nums[i] < key:
            pList.append(nums[i])
        elif nums[i] > key:
            aList.append(nums[i])
        else:
            list.append(nums[i])
    return quick_sort(pList) + list + quick_sort(aList)


def quick_sort1(nums):
    if len(nums) <= 1:
        return nums
    l, r, key = 0, len(nums) - 1, nums[0]
    while l < r:
        while l < r and nums[r] >= key:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] <= key:
            l += 1
        nums[r] = nums[l]
    nums[r] = key
    s1 = quick_sort1(nums[:l])
    s2 = quick_sort1(nums[l + 1:])
    return s1 + [key] + s2


def quick_sort2(nums, left, right):
    if left >= right:
        return nums
    l, r, key = left, right, nums[left]
    while l < r:
        while l < r and nums[r] >= key:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] <= key:
            l += 1
        nums[r] = nums[l]
    nums[l] = key
    quick_sort2(nums, left, l - 1)
    quick_sort2(nums, l + 1, right)
    return nums


if __name__ == '__main__':
    nums = [19, 5, 32, 4, 9, 5, 75, 42, 12, 4, 2, 9]
    haha = quick_sort2(nums, 0, len(nums) - 1)
    print(haha)
