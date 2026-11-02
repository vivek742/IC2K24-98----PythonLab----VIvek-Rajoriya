# 🌟 Lab 8 — Python Dictionary Programs

Five interactive programs for practicing Python dictionaries and related concepts. Each program asks you to enter data while it runs. The data is kept in memory and is cleared when you exit.

## 🚀 Getting started

You need **Python 3**. Open a terminal in the folder containing the files and run one of these commands:

```bash
python student_database.py
python employee_database.py
python library_system.py
python word_frequency.py
python phone_directory.py
```

If your computer uses `python3` to start Python 3, replace `python` with `python3`.

---

## 🎓 Student Database — `student_database.py`

Add students, enter subject marks, update or delete records, and view averages and grade reports.

**Sample interaction:**

```text
STUDENT MENU: 1 Add  2 Update marks  3 Delete  4 Show  5 Reports  6 Exit
Choose: 1
Roll number: 101
Student name: Asha
How many subjects? 2
Subject name: Math
Marks (0-100): 88
Subject name: Science
Marks (0-100): 92
Student added.
```

**Concepts used:** Nested dictionaries, functions, loops, input, averages, conditionals, and grade classification.

---

## 🧑‍💼 Employee Database — `employee_database.py`

Manage employee records and view department payroll, employee salary order, raise calculations, and average salary reports.

**Sample interaction:**

```text
EMPLOYEE MENU: 1 Add  2 Update salary  3 Delete  4 Search  5 Reports  6 Exit
Choose: 1
Employee ID: E1
Name: Kiran
Department: IT
Salary: 60000
Employee added.
```

**Concepts used:** Dictionaries, grouping and totals, `sorted()`, loops, and dictionary comprehensions.

---

## 📚 Library Record System — `library_system.py`

Add books and copies, issue and return books, search records, and view reports. Members can hold up to two books and cannot borrow the same book twice at once.

**Sample interaction:**

```text
LIBRARY MENU: 1 Add book  2 Issue  3 Return  4 Search  5 Reports  6 Exit
Choose: 1
Book ID / ISBN: B1
Number of copies to add: 2
Title: Python Basics
Author: Rao
Book added.
```

**Concepts used:** Nested dictionaries, lists, membership checks, loops, and updating records.

---

## 🔤 Word Frequency Counter — `word_frequency.py`

Enter a paragraph to count words. The program ignores capitalization and punctuation, displays frequent words, groups words, and lets you search for a word.

**Sample interaction:**

```text
Enter a paragraph: The cat and the hat
Counts: {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}
How many top words? 2
Top words: [('the', 2), ('and', 1)]
Words appearing once: ['cat', 'and', 'hat']
```

**Concepts used:** Strings, dictionaries as counters, `.get()`, sorting, and grouping.

---

## 📱 Phone Directory — `phone_directory.py`

Add and update contacts, search by part of a name, look up a contact by phone number, and view contacts grouped by city.

**Sample interaction:**

```text
PHONE MENU: 1 Add contact  2 Add number  3 Update email/city
4 Delete contact  5 Search name  6 Reports  7 Exit
Choose: 1
Name: Anita
10-digit phone number: 9876543210
Email: anita@mail.com
City: Pune
Contact added.
```

**Concepts used:** Nested dictionaries, lists, validation, partial-name search, and reverse lookup.

---

## 📝 Written exercises

- `partb.txt` — Dictionary output predictions and explanations.
- `partc.txt` — Short answers about dictionary copying, keys, lookups, iteration, and performance.

> Sample interactions are examples; your results depend on the information you enter.
