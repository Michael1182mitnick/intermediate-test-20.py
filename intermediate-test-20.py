# Write a program to find the kth largest element in an unsorted array.

import random


def partition(nums, left, right):
    pivot_index = random.randint(left, right)  # Choose a random pivot
    pivot = nums[pivot_index]
    # Move pivot to the end
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    store_index = left

    # Move all smaller elements to the left of the pivot
    for i in range(left, right):
        if nums[i] > pivot:  # We want the kth largest, so we use '>' for descending order
            nums[store_index], nums[i] = nums[i], nums[store_index]
            store_index += 1

    # Move pivot to its final place
    nums[store_index], nums[right] = nums[right], nums[store_index]

    return store_index


def quickselect(nums, left, right, k):
    """
    This function returns the k-th largest element of list within nums[left:right+1]
    """
    if left == right:  # If the list contains only one element
        return nums[left]

    # Select a random pivot_index between left and right
    pivot_index = partition(nums, left, right)

    # The pivot is in its final sorted position
    if k == pivot_index:
        return nums[k]
    elif k < pivot_index:
        # Go left
        return quickselect(nums, left, pivot_index - 1, k)
    else:
        # Go right
        return quickselect(nums, pivot_index + 1, right, k)


def find_kth_largest(nums, k):
    """
    Returns the kth largest element in an array.
    """
    return quickselect(nums, 0, len(nums) - 1, k - 1)


# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(f"The {k}th largest element is {find_kth_largest(nums, k)}")
