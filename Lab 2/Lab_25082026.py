#star pattern
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()


 #matrix op

matrix = []

print("Enter 9 elements:")

for i in range(3):
    row = []

    for j in range(3):
        value = int(input("Enter element: "))
        row.append(value)

    matrix.append(row)


# Display matrix
print("\nMatrix:")

for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()


# Sum of all elements
total = 0

for i in range(3):
    for j in range(3):
        total = total + matrix[i][j]

print("\nSum of all elements:", total)


# Sum of main diagonal
diagonal_sum = 0

for i in range(3):
    diagonal_sum = diagonal_sum + matrix[i][i]

print("Sum of main diagonal:", diagonal_sum)


# Largest and smallest element
largest = matrix[0][0]
smallest = matrix[0][0]

for i in range(3):
    for j in range(3):

        if matrix[i][j] > largest:
            largest = matrix[i][j]

        if matrix[i][j] < smallest:
            smallest = matrix[i][j]

print("Largest element:", largest)
print("Smallest element:", smallest)


# Transpose
print("\nTranspose:")

for i in range(3):
    for j in range(3):
        print(matrix[j][i], end=" ")
    print()