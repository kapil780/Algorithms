def ternary_search(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if key == arr[mid1]:
            return mid1
        if key == arr[mid2]:
            return mid2
        if key < arr[mid1]:
            r = mid1 - 1
        elif key > arr[mid2]:
            l = mid2 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1

array = list(map(int,input("Enter the list in ascending order: ").split()))
x = int(input("Enter the key to find: "))
a = ternary_search(array,x)
print(f"{x} is at index {a} in {array}")
