# 🔢 Concentric Number Square Pattern in Python

## 📌 Project Overview

This Python program generates a **Concentric Number Square Pattern** based on a positive integer entered by the user.

The pattern consists of numbers arranged in square layers, where the outermost layer contains the largest number (`n`) and each inner layer decreases by 1 until the center reaches `1`.

For example, if the user enters `4`, the program generates a square pattern of size `7 × 7`.

## ✨ Features

- Takes user input dynamically.
- Validates input to accept only positive integers.
- Handles invalid inputs using exception handling.
- Generates a concentric square number pattern.
- Uses nested loops and the `min()` function.
- Automatically calculates the pattern size.

## 💻 Sample Output

**Input:**
```text
Enter the number: 4
```

**Output:**
```text
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
```

## ⚙️ How It Works

1. The program takes a positive integer `n` as input.
2. It calculates the square dimensions using:

   `size = 2 * n - 1`

3. Nested loops iterate through every row and column.
4. The `min()` function calculates the minimum distance of the current position from the four edges.
5. The number at each position is calculated using:

   `value = n - distance_from_edge`

6. Finally, the `print()` function displays the pattern.

## 🧠 Concepts Used

- Python Functions
- User Input (`input()`)
- Type Conversion (`int()`)
- Exception Handling (`try-except`)
- Conditional Statements
- While Loop
- Nested For Loops
- Built-in `min()` Function
- Mathematical Logic



