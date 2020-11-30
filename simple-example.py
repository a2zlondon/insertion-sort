A = [222,34,45,45,78,67,1,43,54,656]
print(A)
for current in range(1, len(A)):
    print(current)
    i = current
    while i > 0 and A[i - 1] > A[i]:
        temp = A[i-1]
        A[i-1] = A[i]
        A[i] = temp
        i = i - 1

print(A)
