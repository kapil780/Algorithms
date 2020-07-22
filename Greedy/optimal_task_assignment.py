A = [6,3,2,7,5,5]
A = sorted(A)
max_job = 0
for i in range(len(A)//2):
    if A[i]+A[~i] > max_job:
        max_job = A[i] + A[~i]
print(max_job)