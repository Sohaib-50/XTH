from typing import List


def find_start_end(nums: List[int], target: int) -> List[int]:
    '''
    logic:
        Use binary search to find both, the first and last occurances

    Time complexity: O(LogN)
    Space complexity (O(1))
    '''
    start_idx = -1
    end_idx = -1

    # binary search to find first occurance
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            if (mid == 0) or (nums[mid - 1] != target):
                start_idx = mid
                break
            else:
                right -= 1

        elif nums[mid] > target:
            right -= 1
        else:
            left += 1

    if start_idx == -1:
        return [-1, -1]

    # binary search to last first occurance
    left = start_idx
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            if (mid == len(nums) - 1) or (nums[mid + 1] != target):
                end_idx = mid
                break
            else:
                left += 1

        elif nums[mid] > target:
            right -= 1
        else:
            left += 1

    return [start_idx, end_idx]


print(find_start_end([5, 7, 7, 8, 8, 10], 8))
print(find_start_end([5, 7, 7, 8, 9, 10], 8))
print(find_start_end([5, 7, 7, 8, 9, 10], 199))
print(find_start_end([5, 7, 7, 8, 9, 10], 6))
print(find_start_end([5, 7, 7, 8, 9, 10], 2))
print(find_start_end([5, 7, 7, 8, 9, 10], 5))
print(find_start_end([5, 7, 7, 8, 9, 10], 10))


