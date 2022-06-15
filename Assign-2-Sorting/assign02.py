from queue import Empty
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


def mergeSort(list_items, split_by_3=False):
    """Checks if splitting by 2 or 3 and returns sorted
    Source:
    problem solving with algorithms and data structures using python 3rd ed.
    pg 174 - 176
    """
    start_time = time.time()
    if not split_by_3:
        mergeSortTwo(list_items)
    if split_by_3:
        mergeSort3(list_items)
    elapsed_time = time.time() - start_time
    return (list_items, elapsed_time)


def mergeSortTwo(list_items):
    """This function splits list_of_items recurively.
    Then returns each sublist recursively and iteratively
    sorts.
    """
    if len(list_items) > 1:
        m = mergeSplitTwo(len(list_items))
        list_lo = list_items[:m]
        list_hi = list_items[m:]

        mergeSortTwo(list_lo)
        mergeSortTwo(list_hi)
        lo, hi, i = 0, 0, 0
        while lo < len(list_lo) and hi < len(list_hi):
            if list_lo[lo] < list_hi[hi]:
                list_items[i] = list_lo[lo]
                lo += 1
            else:
                list_items[i] = list_hi[hi]
                hi += 1
            i += 1
        list_items[i:] = list_lo[lo:] or list_hi[hi:]
    return list_items


def mergeSplitTwo(m):
    if m % 2 == 0:
        m = m // 2
    else:
        m = (m + 1) // 2
    return m


def mergeSort3(list_items):
    """Recursively splits list_of_items into thirds, while checking for an
    even or odd length. Then iteratively and recursively sorts
    """
    if len(list_items) > 1:
        split = mergeSplitThree(len(list_items))
        list_lo = list_items[:split]
        list_mid = list_items[split:split * 2]
        list_hi = list_items[split * 2:]

        mergeSort3(list_lo)
        mergeSort3(list_mid)
        mergeSort3(list_hi)

        lo, mid, hi, i = 0, 0, 0, 0
        while lo < len(list_lo) and hi < len(list_hi) and mid < len(list_mid):
            list_items[i] = min(list_lo[lo], list_mid[mid], list_hi[hi])
            if list_items[i] == list_lo[lo]:
                lo += 1
            elif list_items[i] == list_mid[mid]:
                mid += 1
            else:
                hi += 1
            i += 1

        while lo < len(list_lo) and mid < len(list_mid):
            list_items[i] = min(list_lo[lo], list_mid[mid])
            if list_items[i] == list_lo[lo]:
                lo += 1
            else:
                mid += 1
            i += 1

        while lo < len(list_lo) and hi < len(list_hi):
            list_items[i] = min(list_lo[lo], list_hi[hi])
            if list_items[i] == list_lo[lo]:
                lo += 1
            else:
                hi += 1
            i += 1

        while mid < len(list_mid) and hi < len(list_hi):
            list_items[i] = min(list_mid[mid], list_hi[hi])
            if list_items[i] == list_mid[mid]:
                mid += 1
            else:
                hi += 1
            i += 1
        list_items[i:] = list_lo[lo:] or list_mid[mid:] or list_hi[hi:]

    return list_items


def mergeSplitThree(split):
    if split % 2 == 0:
        split = (split + 1) // 3
    else:
        split = split // 3
    return split


def quickSort(list_of_items, pivot_to_use='first'):
    """Determines if sorting by first value or middle value."""
    start_time = time.time()
    if pivot_to_use == 'first':
        qs_first(list_of_items, 0, len(list_of_items))
    if pivot_to_use == 'middle':
        qs_mid(list_of_items, 0, len(list_of_items))
    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


def part_first(arr, lo, hi):
    """[Insert summary]"""
    i, p = lo + 1, arr[lo]
    for j in range(i, hi):
        if arr[j] < p:
            arr[i], arr[j], i = arr[j], arr[i], i + 1
    arr[lo], arr[i - 1] = arr[i - 1], arr[lo]
    return i - 1


def qs_first(arr, lo, hi):
    """[Insert summary]"""
    if lo < hi:
        p = part_first(arr, lo, hi)
        qs_first(arr, lo, p), qs_first(arr, p + 1, hi)


def qs_mid(arr, lo: int, hi: int):
    """[Insert summary]"""
    if (hi - lo) <= 1:
        return
    p = part_mid(arr, lo, hi)
    qs_mid(arr, lo, p), qs_mid(arr, p + 1, hi)


def part_mid(arr, lo, hi):
    """[Insert summary]"""
    arr[hi - 1], arr[(hi + lo - 1) // 2], i = arr[(hi + lo - 1) // 2],\
        arr[hi - 1], lo
    for j in range(lo, hi):
        if arr[j] < arr[hi - 1]:
            arr[i], arr[j], i = arr[j], arr[i], i + 1
    arr[hi - 1], arr[i] = arr[i], arr[hi - 1]
    return i


def radixSort(list_of_items, max_digit):
    """Finds largest element in array and sorts the smallest digit
    to the largest digit in their respective arrays. Calls
    counts for each sub array. Adjusting while loop to fix time constrant.
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

    # list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20, 11, 82, 45, 67, 9]

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
