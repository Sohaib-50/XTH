


from typing import List


def test_three_sum(nums: List[int], target: int) -> bool:
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i != j and j != k and k != i:
                    if nums[i] + nums[j] + nums[k] == target:
                        return True
    return False




def three_sum(nums: List[int], target: int) -> bool:
    '''
    Takes a list of numbers `nums` and a target number `target as input.
    Returns True if a unique triplet exists in nums that adds up to target.
    
    Assuming duplicates within triplets arent allowed.

    Logic:
    Go over the list of numbers, considering a single number at a time. For each
    of that currently considered number try to find two numbers from rest of array
    that add up to remaining required value (i.e. target - that number). Sort the
    array initially for making finding the remaining numbers an easier and faster,
    which can be done using a 2 pointers approach.
    '''
    nums.sort()  # sort for easier searching

    for i in range(len(nums)):

        remaining = target - nums[i]

        # Find 2 numbers in rest of array summing up to `remaining`
        left = i + 1
        right = len(nums) - 1
        while left < right:

            # Stop looking further if found a satisfying triplet
            if nums[left] + nums[right] == remaining:
                return True
            
            # move left pointer ahead to increase sum if sum is less than target
            if nums[left] + nums[right] < remaining:
                left += 1

            # move right pointer behind to decrease sum if sum is less than target
            else:
                right -= 1

    # no satisfying triplet found after the whole process
    return False


# Testing:
print(three_sum([-1, 0, 1, 2, -1, -4], 0))
print(three_sum([1, 2, 3, 4, 5], 10))
print(three_sum([10, 20, 30], 190))


# Time Complexity:
# O(N^2) 
#     - O(NLogN) for sorting
#     - O(N) for the first loop
#     - O(N) for the 2nd (nested) loop
#     - O(N^2) for the nested loops structure
#     - O(NLogN) + O(N^2) =  O(N^2)!

# Space Complexity:
# O(1)
#     - Using only single variables, no datastructure that varies size with input.
#     - Considering the sort function doesnt use any extra space.


        













print(test_three_sum([1, 2, 3, 4], 1) == three_sum([1, 2, 3, 4], 1))
print(test_three_sum([-1, 0, 1, 2, -1, -4], 0) ==  three_sum([-1, 0, 1, 2, -1, -4], 0))
print(test_three_sum([1, 2, 3, 4, 5], 10) == three_sum([1, 2, 3, 4, 5], 10))
print(test_three_sum([10, 20, 30], 190) == three_sum([10, 20, 30], 190))



print()

