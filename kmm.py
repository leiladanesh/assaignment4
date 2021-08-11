n = int(input())
m = int(input())

for i in range(m,n*m+1):
    if i % n == 0 and i % m == 0:
        kmm =i
print(kmm)