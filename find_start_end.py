from typing import List


def find_start_end(nums: List[int], target: int) -> List[int]:

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            break
        elif nums[mid] > target:
            right -= 1
        else:
            left += 1

    if nums[mid] != target:
        return [-1, -1]
    
    start_idx = mid
    while (start_idx > 0) and (nums[start_idx - 1] == target):
        start_idx -= 1

    end_idx = mid
    while (end_idx < len(nums) - 1) and (nums[end_idx + 1] == target):
        end_idx += 1

    return [start_idx, end_idx]


print(find_start_end([5, 7, 7, 8, 8, 10], 8))
print(find_start_end([5, 7, 7, 8, 9, 10], 8))
print(find_start_end([5, 7, 7, 8, 9, 10], 199))
print(find_start_end([5, 7, 7, 8, 9, 10], 6))
print(find_start_end([5, 7, 7, 8, 9, 10], 2))
print(find_start_end([5, 7, 7, 8, 9, 10], 5))
print(find_start_end([5, 7, 7, 8, 9, 10], 10))


# logic:
# first find any occurance of the target using bubble sort.
# If not found return -1, -1
# if found then to find first occurance move left from mid till first occurance of target
# and to find end move right from mid till last occurance.

# Actually wanted to find both start and end with bubble sort, but couldnt due to shortage of time.
