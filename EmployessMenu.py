from Employees import Employee, Manager
from Validator import get_valid


def manage_employees(employees_dict):
    while True:
        # print()
        print("=" * 50)
        print("            Employee Management")
        print("=" * 50)
        print()

        # menu
        print("1.1 Add New Employee")
        print("1.2 View All Employees")
        print("1.3 Update Employee Details")
        print("1.4 Delete Employee")
        print("1.5 Back To Main Menu")
        print()

        choice = input("Please enter your choice: ").strip()
        if choice == "1":
            name =get_valid("Enter Name: ", str)
            role = get_valid("Enter Role: ", str).capitalize()
            salary = get_valid("Enter Salary: ", float)
            if role not in ["Manager", "Staff"]:
                print("Wrong Role, setting it to default staff")
                role = "Staff"
            if not employees_dict:
                new_id = "E101"
                # E101 => 101
            else:
                last_id = max(int(eid[1:]) for eid in employees_dict.keys() )
                new_id = f"E{last_id + 1}"

            if role == "Manager":
                new_emp = Manager(new_id, name,role, salary, bonus = 1000.00 )
            else:
                new_emp = Employee(new_id, name,role, salary)

            employees_dict[new_id] = new_emp
            print(f"{name} added with Id {new_id}")
            input("Press any key to continue...")
        elif choice == "2":
            print()
            print("+" * 50)
            print("       All Employee Details")
            print("+" * 50)
            print()
            for emp in employees_dict.values():
                print(emp.get_details())
                print('-' * 50)
            print()
            input("Press any key to continue...")
        elif choice == "3":
            if not employees_dict:
                print("No employees found! Add some employees first")
                print()
                input("Press any key to continue...")
                continue

            print('+' * 50)
            print("              Update Employee Details")
            print("+" * 50)
            print()

            empy_id_to_update = get_valid("Enter Employee ID to update: ", str)
            if empy_id_to_update in employees_dict.keys():
                empy_data = employees_dict[empy_id_to_update]

                print("Employee To Update")
                print(empy_data.get_details())
                print()
                while True:
                    print()
                    print('1.1 Update Employee Name')
                    print('1.2 Update Employee Salary')
                    if empy_data.role == "Manager":
                        print('1.3 Update Employee Bonus')
                    print('1.4 Go back to Employee Management Menu')
                    print()
                    choice = input("Please enter your choice: ").strip()
                    if choice == "1":
                        new_name = get_valid("Enter New Employee Name: ", str )
                        empy_data.name = new_name
                    elif choice == "2":
                        new_salary = get_valid("Enter New Employee Salary: ",float)
                        empy_data.salary = new_salary
                    elif choice == "3":
                        new_bonus = get_valid("Enter New Employee Bonus: ",float)
                        empy_data.bonus = new_bonus
                    elif choice == "4":
                        print(empy_data.get_details())
                        employees_dict[empy_id_to_update] = empy_data
                        print("Going Back to Employee Management Menu")
                        input("Press any key to continue...")
                        break
                    else:
                        print("Wrong Choice, Select From 1 to 4 only in numeric form")

            else:
                print("Wrong Employee ID")
            input("Press any key to continue...")

        elif choice == "4":
            print("Delete Employee")
        elif choice == "5":
            print("------ Going Back to Main Menu")
            break
        else:
            print("Please enter a valid choice 1 to 5 only in numeric form")

