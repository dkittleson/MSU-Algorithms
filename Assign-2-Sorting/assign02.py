import time
import random
import sys
from math import ceil, log10

# Set recursion limit to be greater than the max size of any
# list you attempt to sort
sys.setrecursionlimit(10000)


def bubbleSort(list_of_items):
    """Iterates through lists comparing values and exchanging
    with neighboring values until it is bigger than the value
    value to its left, but smaller than the value to its
    right. Source:
    problem solving with algorithms and data structures using python 3rd ed.
    pg 164
    """
    start_time = time.time()

    for pass_list in range(len(list_of_items) - 1, 0, -1):
        for i in range(pass_list):
            if list_of_items[i] > list_of_items[i + 1]:
                swapAdj(list_of_items, i)

    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


def swapAdj(list_swap, x):
    """Swap adjacent variables"""
    temp_list = list_swap[x]
    list_swap[x] = list_swap[x + 1]
    list_swap[x + 1] = temp_list


def swap2(list_swap, from_idx, to_idx):
    """Swap variables at two locations"""
    temp = list_swap[from_idx]
    list_swap[from_idx] = list_swap[to_idx]
    list_swap[to_idx] = temp


def mergeSort(list_of_items, split_by_3=False):
    """Checks if splitting by 2 or 3 and returns sorted
    Source:
    problem solving with algorithms and data structures using python 3rd ed.
    pg 174 - 176
    """
    start_time = time.time()
    if not split_by_3:
        mergeSort2(list_of_items)
    if split_by_3:
        mergeSort3(list_of_items)
    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


def mergeSort2(list_of_items):
    """This function splits list_of_items recurively.
    Then returns each sublist recursively and iteratively
    sorts.
    """
    if len(list_of_items) > 1:
        if len(list_of_items) % 2 == 0:
            mid = len(list_of_items) // 2
        else:
            mid = (len(list_of_items) + 1) // 2
        low_half = list_of_items[:mid]
        high_half = list_of_items[mid:]

        mergeSort2(low_half)
        mergeSort2(high_half)

        i, j, k = 0, 0, 0

        while i < len(low_half) and j < len(high_half):
            if low_half[i] < high_half[j]:
                list_of_items[k] = low_half[i]
                i += 1
            else:
                list_of_items[k] = high_half[j]
                j += 1
            k += 1

        while i < len(low_half):
            list_of_items[k] = low_half[i]
            i += 1
            k += 1

        while j < len(high_half):
            list_of_items[k] = high_half[j]
            j += 1
            k += 1
    return list_of_items


def mergeSort3(list_of_items):
    """Recursively splits list_of_items into thirds, while checking for an
    even or odd length. Then iteratively and recursively sorts
    """
    if len(list_of_items) > 1:
        if len(list_of_items) % 2 == 0:
            split = (len(list_of_items) + 1) // 3
        else:
            split = len(list_of_items) // 3
        low_list = list_of_items[:split]
        mid_list = list_of_items[split:split * 2]
        high_list = list_of_items[split * 2:]

        mergeSort3(low_list)
        mergeSort3(mid_list)
        mergeSort3(high_list)

        i, k, j, g = 0, 0, 0, 0
        # NEEDS ONE TO SORT FULLY
        while i < len(low_list) and j < len(high_list) and g < len(mid_list):
            #  Low and Mid
            if low_list[i] < high_list[j] and mid_list[g] < high_list[j]:
                if low_list[i] < mid_list[g]:
                    list_of_items[k] = low_list[i]
                    i += 1
                elif low_list[i] > mid_list[g]:
                    list_of_items[k] = mid_list[g]
                    g += 1
                k += 1

            #  Mid and High
            elif mid_list[g] < low_list[i] and high_list[j] < low_list[i]:
                if high_list[j] < mid_list[g]:
                    list_of_items[k] = high_list[j]
                    j += 1
                elif high_list[j] > mid_list[g]:
                    list_of_items[k] = mid_list[g]
                    g += 1
                k += 1

            #  High and Low
            elif high_list[j] < mid_list[g] and low_list[i] < mid_list[g]:
                if low_list[i] < high_list[j]:
                    list_of_items[k] = low_list[i]
                    i += 1
                elif low_list[i] > high_list[j]:
                    list_of_items[k] = high_list[j]
                    j += 1
                k += 1

        # low and mid
        while i < len(low_list) and g < len(mid_list):
            if low_list[i] < mid_list[g]:
                list_of_items[k] = low_list[i]
                i += 1
            elif low_list[i] > mid_list[g]:
                list_of_items[k] = mid_list[g]
                g += 1
            k += 1

        # low and high
        while i < len(low_list) and j < len(high_list):
            if low_list[i] < high_list[j]:
                list_of_items[k] = low_list[i]
                i += 1
            elif low_list[i] > high_list[j]:
                list_of_items[k] = high_list[j]
                j += 1
            k += 1

        # Mid and High
        while j < len(high_list) and g < len(mid_list):
            if high_list[j] < mid_list[g]:
                list_of_items[k] = high_list[j]
                j += 1
            elif high_list[j] > mid_list[g]:
                list_of_items[k] = mid_list[g]
                g += 1
            k += 1

        # just low
        while i < len(low_list):
            list_of_items[k] = low_list[i]
            i += 1
            k += 1

        # just mid
        while g < len(mid_list):
            list_of_items[k] = mid_list[g]
            g += 1
            k += 1

        # just high
        while j < len(high_list):
            list_of_items[k] = high_list[j]
            j += 1
            k += 1

    return list_of_items


def quickSort(list_of_items, pivot_to_use='first'):
    """Determines if sorting by first value or middle value.
    Source:
    problem solving with algorithms and data structures using python 3rd ed.
    pg 178 - 179
    """
    start_time = time.time()
    end_index = len(list_of_items) - 1
    if pivot_to_use == 'first':
        quicksort_helper(list_of_items, 0, end_index, partition_first)
    if pivot_to_use == 'middle':
        quicksort_helper(list_of_items, 0, end_index, partition_mid)
    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


def quicksort_helper(list_of_items, low, high, partition_func):
    """Used to recursively call partion, utilizing quicksort_helper
    to use the first element as a split point
    """
    if low < high:
        split = partition_func(list_of_items, low, high)
        quicksort_helper(list_of_items, low, split - 1, partition_func)
        quicksort_helper(list_of_items, split + 1, high, partition_func)


def partition_first(list_of_items, low, high):
    """Uses first value in list as pivot, the swaps pivot or values"""
    pivot = list_of_items[low]
    left_mark = low + 1
    right_mark = high
    while True:
        while left_mark <= right_mark and list_of_items[left_mark] < pivot:
            left_mark += 1
        while left_mark <= right_mark and list_of_items[right_mark] > pivot:
            right_mark -= 1
        if left_mark >= right_mark:
            # swap pivot to correct location
            tmp = list_of_items[low]
            list_of_items[low] = list_of_items[right_mark]
            list_of_items[right_mark] = tmp

            return right_mark

        # swap the wrong locations
        tmp = list_of_items[left_mark]
        list_of_items[left_mark] = list_of_items[right_mark]
        list_of_items[right_mark] = tmp

        # left_mark += 1
        # right_mark -= 1


def partition_mid(list_of_items, low, high):
    """Uses middle value as pivot, then swaps values"""
    pivot = list_of_items[(low + high + 1) // 2]
    left_mark = low
    right_mark = high
    while True:
        while left_mark <= right_mark and list_of_items[left_mark] < pivot:
            left_mark += 1
        while left_mark <= right_mark and list_of_items[right_mark] > pivot:
            right_mark -= 1
        if left_mark >= right_mark:
            return right_mark

        # swap the wrong locations
        tmp = list_of_items[left_mark]
        list_of_items[left_mark] = list_of_items[right_mark]
        list_of_items[right_mark] = tmp


def radixSort(list_of_items, max_digit):
    """Finds largest element in array and sorts the smallest digit
    to the largest digit in their respective arrays. Calls
    counts for each sub array. Adjusting while loop to fix time constrant.
    Source:
    alphacodingskills.com/python/pages/python-program-for-radix-sort.php
    """
    start_time = time.time()
    place = 1
    while (max_digit / place) > (1 / (100 * max_digit)):
        countingsort(list_of_items, place)
        place *= 10
    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


def countingsort(list_of_items, place):
    """Sort is dependent on digit's place and builds
    lists for n number of digits and their frequency
    """
    n = len(list_of_items)
    output = [0 for i in range(0, n)]
    freq = [0 for i in range(0, 10)]

    for i in range(0, n):
        freq[(list_of_items[i] // place) % 10] += 1
    for i in range(1, 10):
        freq[i] += freq[i - 1]
    for i in range(n - 1, -1, -1):
        output[freq[(list_of_items[i] // place) % 10] - 1] = list_of_items[i]
        freq[(list_of_items[i] // place) % 10] -= 1
    for i in range(0, n):
        list_of_items[i] = output[i]


def assign02_main():
    """ A 'main' function to be run when our program is run standalone """
    list1 = list(range(5000))
    random.seed(1)
    random.shuffle(list1)

    # list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20, 11]

    # run sorting functions
    bubbleRes = bubbleSort(list(list1))
    mergeRes2 = mergeSort(list(list1), split_by_3=False)
    mergeRes3 = mergeSort(list(list1), split_by_3=True)
    quickResA = quickSort(list(list1), pivot_to_use='first')
    quickResB = quickSort(list(list1), pivot_to_use='middle')
    radixRes = radixSort(list(list1), ceil(log10(max(list1))))

# Print results
    print(f"\n\nlist1 results (randomly shuffled w/ size = {len(list1)})")
    print(list1[:10])
    print(f"\n  bubbleSort time: {bubbleRes[1]:.10f} sec")
    print(bubbleRes[0][:10])
    print(f"\n  mergeSort2 time: {mergeRes2[1]:.8f} sec")
    print(mergeRes2[0][:10])
    print(f"\n  mergeSort3 time: {mergeRes3[1]:.8f} sec")
    print(mergeRes3[0][:10])
    print(f"\n  quickSortA time: {quickResA[1]:.8f} sec")
    print(quickResA[0][:10])
    print(f"\n  quickSortB time: {quickResB[1]:.8f} sec")
    print(quickResB[0][:10])
    print(f"\n  radixSort time: {radixRes[1]:.8f} sec")
    print(radixRes[0][:10])

    # Try with a list sorted in reverse order (worst case for quicksort)
    list2 = list(range(6000, 1000, -1))

    # list2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    # run sorting functions
    bubbleRes = bubbleSort(list(list2))
    mergeRes2 = mergeSort(list(list2), split_by_3=False)
    mergeRes3 = mergeSort(list(list2), split_by_3=True)
    quickResA = quickSort(list(list2), pivot_to_use='first')
    quickResB = quickSort(list(list2), pivot_to_use='middle')
    radixRes = radixSort(list(list2), ceil(log10(max(list2))))

    # Print results
    print(f"\n\nlist2 results (sorted in reverse w/ size = {len(list2)})")
    print(list2[:10])
    print(f"\n  bubbleSort time: {bubbleRes[1]:.8f} sec")
    print(bubbleRes[0][:10])
    print(f"\n  mergeSort2 time: {mergeRes2[1]:.8f} sec")
    print(mergeRes2[0][:10])
    print(f"\n  mergeSort3 time: {mergeRes3[1]:.8f} sec")
    print(mergeRes3[0][:10])
    print(f"\n  quickSortA time: {quickResA[1]:.8f} sec")
    print(quickResA[0][:10])
    print(f"\n  quickSortB time: {quickResB[1]:.8f} sec")
    print(quickResB[0][:10])
    print(f"\n  radixSort time: {radixRes[1]:.8f} sec")
    print(radixRes[0][:10])


# Check if the program is being run directly (i.e. not being imported)
if __name__ == '__main__':
    assign02_main()