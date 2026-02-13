N = input()
F = int(input())

N = list(N)  
base = N[:-2]  

for i in range(10):      
    for j in range(10):  
        N[-2] = str(i)
        N[-1] = str(j)

        num = int("".join(N))

        if num % F == 0:
           print(i, end='')
           print(j)
           exit()
