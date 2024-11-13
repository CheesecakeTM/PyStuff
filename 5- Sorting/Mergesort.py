# MERGESORT sorting algorithm

# Mergesort is another divide-and-conquer algorithm that divides the array into halves,
# sorts each half, and then merges the sorted halves back together.
# Steps:
#
#    1- Divide: If the array has more than one element, split it into two halves.
#
#    2- 4- Recursion: Recursively sort each half.
#
#    3- Merge: Combine the two sorted halves into a single sorted array.


# EXAMPLE USE CASE
# array = [38, 27, 43, 3, 9, 82, 10]
# sorted_array = mergesort(array)
# print(sorted_array)
#
# -> Output: [3, 9, 10, 27, 38, 43, 82]


def mergesort(arr):
    if len(arr) <= 1:
        return arr  # Base case: an array with 0 or 1 element is already sorted

    mid = len(arr) // 2  # Find the middle index
    left_half = mergesort(arr[:mid])  # Recursively sort the left half
    right_half = mergesort(arr[mid:])  # Recursively sort the right half

    return merge(left_half, right_half)  # Merge the sorted halves

def merge(left, right):
    sorted_a = []
    i = j = 0

    # Merge the two halves while maintaining order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_a.append(left[i])
            i += 1
        else:
            sorted_a.append(right[j])
            j += 1

    # If there are remaining elements in left or right, add them
    sorted_a.extend(left[i:])
    sorted_a.extend(right[j:])

    return sorted_a
