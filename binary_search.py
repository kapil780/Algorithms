# Works in sorted array
# If two same elements are present then it returns the address of first element
arr = [1, 2, 3, 5, 6, 7]


def binarySearch(array, key):
    l = 0
    r = len(array) - 1
    while l <= r:
        mid = l + (r - l) // 2  # Divide the array in two parts

        if array[mid] < key:  # If key is greater than middle element then look in the 2nd half
            l = mid + 1
        elif array[mid] > key:  # If key is less than middle element then look in the 1st half
            r = mid - 1
        else:
            return array[mid]  # If key is equal to middle element return the posotion
    return z  # If element is not present return -1


print(binarySearch(arr, 4))
