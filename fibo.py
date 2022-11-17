def fibo(n):
    #1 1 2 3 5 8...
    k = 1
    if n==1 or n==2:
        return 1
    else:
       return fibo(n-2)+fibo(n-1)

n = int(input('n='))

for i in range(1,n+1):
    print(fibo(i), end=',')
print()