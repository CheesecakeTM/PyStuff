# here are some random test stuff

from Sorting import Quicksort, Mergesort

array_q = [3, 6, 8, 10, 1, 2, 1]
array_m = [38, 27, 43, 3, 9, 82, 10]

quick_sorted_array = Quicksort.quicksort(array_q)
merge_sorted_array = Mergesort.mergesort(array_m)

print(quick_sorted_array)
print(merge_sorted_array)
