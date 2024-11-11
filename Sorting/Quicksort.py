# QUICKSORT sorting algorithm

# Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning
# the other elements into two sub-arrays according to whether they are less than or greater than the pivot.
# The sub-arrays are then sorted recursively.
# Steps:
#
#    1- Choose a Pivot: Select an element from the array (common choices include the first element,
#                       the last element, or a random element).
#
#    2-Partitioning: Rearrange the array so that elements less than the pivot are on the left
#                    and elements greater than the pivot are on the right.
#
#    3- Recursion: Recursively apply the above steps to the left and right sub-arrays.


# EXAMPLE USE CASE
# array = [3, 6, 8, 10, 1, 2, 1]
# sorted_array = quicksort(array)
# print(sorted_array)
#
# -> Output: [1, 1, 2, 3, 6, 8, 10]


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
