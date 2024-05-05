def recursion(nums: list, target: int):
    def binarysearch(left, right):
        if left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                return binarysearch(mid + 1, right)
            elif nums[mid] > target:
                return binarysearch(left, mid - 1)
            else:
                return mid
        else:
            return -1

    return binarysearch(0, len(nums) - 1)


def iterative(nums: list, target: int):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


def library(nums: list, target: int):
    index = bisect.bisect_left(nums, target)
    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1
