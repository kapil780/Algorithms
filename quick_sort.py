arr = [4, 2, -1, 6, 4, 8]


def quickSort(array, left, right):
    if left < right:
        pi = partition(array, left, right)
        quickSort(array, left, pi - 1)
        quickSort(array, pi + 1, right)


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[right]) = (arr[right], arr[i + 1])
    return i + 1  # Now the pivot is in the right place so return it's position


quickSort(arr, 0, len(arr) - 1)
print(arr)
