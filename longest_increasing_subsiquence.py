def lis(arr):
    n = len(arr)
    temp_arr = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and temp_arr[i] < temp_arr[j] + 1:
                temp_arr[i] = temp_arr[j] + 1
    return(max(temp_arr))


m = lis([3, 4, -1, 0, 6, 2, 3])
print(m)
