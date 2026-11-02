# Student Database
# Functions keep each menu task in a small, named part.


def get_marks():
    marks = {}
    how_many = int(input("How many subjects? "))
    for number in range(how_many):
        subject = input("Subject name: ")
        score = float(input("Marks (0-100): "))
        while score < 0 or score > 100:
            print("Marks must be between 0 and 100.")
            score = float(input("Marks (0-100): "))
        marks[subject] = score
    return marks


def add_student(students):
    roll = input("Roll number: ")
    if roll in students:
        print("That roll number already exists.")
        return
    name = input("Student name: ")
    students[roll] = {"name": name, "marks": get_marks()}
    print("Student added.")


def update_marks(students):
    roll = input("Roll number: ")
    if roll not in students:
        print("Student not found.")
        return
    subject = input("Subject: ")
    score = float(input("New marks (0-100): "))
    while score < 0 or score > 100:
        print("Marks must be between 0 and 100.")
        score = float(input("New marks (0-100): "))
    students[roll]["marks"][subject] = score
    print("Marks updated.")


def show_reports(students):
    if not students:
        print("No students have been added.")
        return
    averages = {}
    for roll, student in students.items():
        marks = student["marks"].values()
        averages[roll] = round(sum(marks) / len(marks), 2) if marks else 0
    print("Averages:", averages)
    topper = max(averages, key=averages.get)
    print("Topper:", students[topper]["name"])

    print("Marks below 40:")
    for student in students.values():
        for subject, score in student["marks"].items():
            if score < 40:
                print(student["name"], subject, score)

    grades = {"A": [], "B": [], "C": [], "D": [], "F": []}
    for roll, average in averages.items():
        if average >= 90: letter = "A"
        elif average >= 75: letter = "B"
        elif average >= 60: letter = "C"
        elif average >= 40: letter = "D"
        else: letter = "F"
        grades[letter].append(students[roll]["name"])
    print("Grade groups:", grades)


def main():
    students = {}
    while True:
        print("\nSTUDENT MENU: 1 Add  2 Update marks  3 Delete  4 Show  5 Reports  6 Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            update_marks(students)
        elif choice == "3":
            roll = input("Roll number: ")
            if roll in students:
                del students[roll]
                print("Student deleted.")
            else:
                print("Student not found.")
        elif choice == "4":
            roll = input("Roll number: ")
            print(students.get(roll, "Student not found."))
        elif choice == "5":
            show_reports(students)
        elif choice == "6":
            break
        else:
            print("Choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
