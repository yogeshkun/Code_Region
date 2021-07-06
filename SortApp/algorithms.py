from django.http import HttpResponse

def linearSearch(arr, key):
    flag = 0
    print('arr = ')
    print(key)
    for i in range(len(arr)):
        if key == arr[i]:
            flag = 1
            return i
    if flag == 0:
        return None


def binarySearch(arr, key):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if key == arr[mid]:
            return mid 
        elif key > arr[mid]:
            low = mid + 1
        elif key < arr[mid]:
            high = mid - 1

    return None


def bubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
# Find the middle point and devide it
    middle = len(arr) // 2
    left_list = arr[:middle]
    right_list = arr[middle:]

    left_list = mergeSort(left_list)
    right_list = mergeSort(right_list)

    return list(merge(left_list, right_list))

# Merge the sorted halves


def merge(left_half, right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    # print(res)
    return res


def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i-1
        nxt_element = arr[i]
# Compare the current element with next one

        while (arr[j] > nxt_element) and (j >= 0):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = nxt_element

    return arr


def selectionSort(arr):
    for i in range(len(arr)):
        min_i = i
        for j in range(i + 1, len(arr)):
            if arr[min_i] > arr[j]:
                min_i = j
# Swap the minimum value with the compared value
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr
########### ALGOS END ############
