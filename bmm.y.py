n = int(input())
m = int(input())

for i in range(1,n+1):
    if n % i == 0 and m % i == 0:
        bmm=i
print(bmm)