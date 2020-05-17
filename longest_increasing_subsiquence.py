def lis(arr):
    n = len(arr)
    temp_arr = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                temp_arr[i] = max(temp_arr[i], temp_arr[j] + 1)
    return(max(temp_arr))


m = lis([10, 22, 9, 33, 21, 50, 41, 60])
print(m)
