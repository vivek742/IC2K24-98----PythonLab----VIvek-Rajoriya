# 🐍 Lab 6 — Python Programs

Five small, interactive programs for practicing Python basics. Run each one separately from a terminal.

## ▶️ Getting started

You need **Python 3**. Open a terminal in the folder containing the files and run:

```bash
python atm_sim.py
```

Replace `atm_sim.py` with `combine_appln.py`, `grade_calc.py`, `guessgame.py`, or `rev_guess.py` to run another program. Some computers use `python3` instead of `python`.

---

## 🏧 ATM Simulation — `atm_sim.py`

**What it does:** Sign in, check a balance, deposit or withdraw money, and change the PIN. The starting balance is ₹5,000 and the initial PIN is `1234`.

**Concepts used:** Functions, `while` loops, `if`/`elif` choices, input validation, numeric conversion, and formatted output.

**Sample output:**

```text
Enter your PIN: 1234
PIN accepted. Welcome!

===== ATM MENU =====
1. Check Balance
2. Deposit
3. Withdraw
4. Change PIN
5. Exit
Enter your choice: 1
Current balance: ₹5000.00
```

---

## 🧰 Combined Application — `combine_appln.py`

**What it does:** A main menu that opens an ATM, grade calculator, or guessing game. Its ATM starts with ₹5,000 and PIN `1234`.

**Concepts used:** Importing Python's `random` module, functions, nested menus, loops, conditionals, dictionaries, lists, validation, and arithmetic.

**Sample output:**

```text
================================
       COMBINED APPLICATION
================================
1. ATM
2. Grade Calculator
3. Guessing Game
4. Exit
Enter your choice: 2

===== GRADE CALCULATOR =====
1. Enter marks for a new student
2. View grade of last entered student
3. Exit
```

---

## 🎓 Grade Calculator — `grade_calc.py`

**What it does:** Takes marks for five subjects, calculates the average, and assigns a grade. You can view the last student's result while the program is running.

**Grade scale:** `A` 90+, `B` 75+, `C` 60+, `D` 40+, otherwise `F`.

**Concepts used:** Functions, lists, loops, input validation, `sum()`, averages, conditionals, and dictionaries.

**Sample output:**

```text
Enter marks for subject 1: 95
Enter marks for subject 2: 85
Enter marks for subject 3: 75
Enter marks for subject 4: 65
Enter marks for subject 5: 80

Student data saved successfully.
Average: 80.00
Grade: B
```

---

## 🎯 Guessing Game — `guessgame.py`

**What it does:** Guess the computer's random number from 1 to 100 in at most seven tries. You start with 100 points and lose 10 for each wrong guess. Hints say higher/lower, even/odd, and whether the number is a multiple of 5.

**Concepts used:** The `random` module, loops, conditionals, input validation, counters, and scoring.

**Sample output:**

```text
I selected a number between 1 and 100.
You have 7 attempts.
You start with 100 points.

Attempt 1 of 7
Enter your guess (1-100): 50
Too low!
Hint: The secret number is even.
Hint: The secret number is a multiple of 5.
```

*The secret number and hints vary each time you play.*

---

## 🔄 Reverse Guessing Game — `rev_guess.py`

**What it does:** Think of a number within limits you choose. The computer guesses, and you tell it whether its guess is too high (`h`), too low (`l`), or correct (`c`).

**Concepts used:** Binary search, integer division, loops, conditionals, functions, and input validation.

**Sample output:**

```text
Enter the lower limit: 1
Enter the upper limit: 100

My guess is: 50
Enter feedback (h = too high, l = too low, c = correct): l

My guess is: 75
Enter feedback (h = too high, l = too low, c = correct): h

My guess is: 62
Enter feedback (h = too high, l = too low, c = correct): c
I guessed your number in 3 guesses!
```

---
