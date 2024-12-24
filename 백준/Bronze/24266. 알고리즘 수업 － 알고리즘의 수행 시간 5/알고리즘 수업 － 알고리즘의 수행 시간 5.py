def MenOfPassion(arr, n) :
    sum = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                sum = sum + arr[i] * arr[j] * arr[k]; 
    return sum

n = int(input())
print(n*n*n)
print(3)