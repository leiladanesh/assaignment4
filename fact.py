def factorial (number):
    fact = 1
    a = 0
    for i in range(number):
        fact = fact * (i+1)
        if fact == number:
            print('YES')
            a = 1
            break

    if a == 0:
            print('No')


number = int(input())
factorial(number)
