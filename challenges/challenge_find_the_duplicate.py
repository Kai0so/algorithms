def find_duplicate(nums):
    nums.sort()
    n = len(nums)
    is_duplicate = -1
    for index in range(0, n - 1):
        if nums[index] == nums[index + 1]:
            is_duplicate = nums[index]
    if is_duplicate < 0:
        return False
    return is_duplicate
