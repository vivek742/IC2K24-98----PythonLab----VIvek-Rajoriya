# Employee Database


def add_employee(employees):
    emp_id = input("Employee ID: ")
    if emp_id in employees:
        print("That ID already exists.")
        return
    name = input("Name: ")
    department = input("Department: ")
    salary = float(input("Salary: "))
    employees[emp_id] = {"name": name, "dept": department, "salary": salary}
    print("Employee added.")


def show_reports(employees):
    if not employees:
        print("No employees have been added.")
        return
    departments = {}
    for employee in employees.values():
        dept = employee["dept"]
        if dept not in departments:
            departments[dept] = {"payroll": 0, "count": 0}
        departments[dept]["payroll"] += employee["salary"]
        departments[dept]["count"] += 1
    print("Payroll and headcount:", departments)

    ordered = sorted(employees.values(), key=lambda person: person["salary"], reverse=True)
    print("Employees by salary:")
    for employee in ordered:
        print(employee["name"], employee["salary"])

    # Build new records so the entered salaries do not change.
    raised = {
        emp_id: {"name": person["name"], "dept": person["dept"],
                 "salary": person["salary"] * 1.10 if person["salary"] < 50000 else person["salary"]}
        for emp_id, person in employees.items()
    }
    print("Salary report after raises:")
    for person in raised.values():
        print(person["name"], person["salary"])

    averages = {}
    for dept, totals in departments.items():
        averages[dept] = totals["payroll"] / totals["count"]
    best_department = max(averages, key=averages.get)
    print("Highest average salary:", best_department, averages[best_department])


def main():
    employees = {}
    while True:
        print("\nEMPLOYEE MENU: 1 Add  2 Update salary  3 Delete  4 Search  5 Reports  6 Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            emp_id = input("Employee ID: ")
            if emp_id in employees:
                employees[emp_id]["salary"] = float(input("New salary: "))
                print("Salary updated.")
            else:
                print("Employee not found.")
        elif choice == "3":
            emp_id = input("Employee ID: ")
            if emp_id in employees:
                del employees[emp_id]
                print("Employee deleted.")
            else:
                print("Employee not found.")
        elif choice == "4":
            emp_id = input("Employee ID: ")
            print(employees.get(emp_id, "Employee not found."))
        elif choice == "5":
            show_reports(employees)
        elif choice == "6":
            break
        else:
            print("Choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
