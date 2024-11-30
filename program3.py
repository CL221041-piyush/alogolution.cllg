import random

def quickselect(nums, left, right, k):
    pivot = random.randint(left, right)
    pivot = partition(nums, left, right, pivot)

    if pivot == k:
        return nums[pivot]
    elif pivot > k:
        return quickselect(nums, left, pivot - 1, k)
    else:
        return quickselect(nums, pivot + 1, right, k)

def partition(nums, left, right, pivot):
    nums[right], nums[pivot] = nums[pivot], nums[right]
    pivot_value = nums[right]
    i = left
    for j in range(left, right):
        if nums[j] >= pivot_value:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i

def findKthLargest(nums, k):
    n = len(nums)
    return quickselect(nums, 0, n - 1, k - 1)

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  
