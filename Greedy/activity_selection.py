list_a = list(map(int,input().split()))
list_b = list(map(int,input().split()))
i = 0
count = 1
print(i)
for j in range(1,len(list_a)):
    if list_b[i] <= list_a[j]:
        print(j)
        count += 1
        i = j
print(count)
