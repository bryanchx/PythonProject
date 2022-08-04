def merge(left, right):
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


def unname(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = unname(nums[:mid])
    right = unname(nums[mid:])
    return merge(left, right)


# return []


if __name__ == '__main__':
    nums = [19, 5, 32, 4, 9, 5, 75, 42, 12, 4, 2, 9]
    print(unname(nums))
