#hollow diamond

n = int(input("Enter an odd number: "))

for i in range(n):
    if i <= n // 2:
        spaces = n // 2 - i
        stars = 2 * i + 1
    else:
        spaces = i - n // 2
        stars = 2 * (n - i) - 1

    for j in range(spaces):
        print(" ", end="")

    for j in range(stars):
        if j == 0 or j == stars - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()

#butterfly pattern
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

    for j in range(i):
        print("*", end="")

    for j in range(2 * (n - i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")

    print()

for i in range(n - 1, 0, -1):

    for j in range(i):
        print("*", end="")

    for j in range(2 * (n - i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")

    print()