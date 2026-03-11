def  print_report(entity_list):
    print("=" * 50)
    print("Generating Comprehensive Report")
    print("=" * 50)
    print()
    for item in entity_list:
        print(item.get_details())
    print("      End of Report ")

def manage_financials(emp_dic, assets_dic):

    while True:
        print("=" * 50)
        print("        Company Financial Menu")
        print("=" * 50)
        print("3.1 Total Salary Expenditure")
        print("3.2 Total Assets Value")
        print("3.3 Generate Full Report")
        print("3.4 Back to Main Menu")

        print()
        choice = input("Enter your choice: ")
        if choice == "1":
            total_bonus = sum(emp.bonus for emp in emp_dic.values() if emp.role == "Manager")
            total_pay = sum(emp.salary for emp in emp_dic.values())
            print(f"Total Monthly Salary: Rs.{total_pay + total_bonus:,.2f}")
            input("Press Enter to continue...")
        elif choice == "2":
            total_value = sum(asset.value for asset in assets_dic.values())
            print(f"Total Assets is Value: Rs.{total_value:,.2f}")
            input("Press Enter to continue...")
        elif choice == "3":
            all_entities = list(emp_dic.values()) + list(assets_dic.values())
            print_report(all_entities)
            input("Press Enter to continue...")
        elif choice == "4":
            print("Going Back To Main Menu")
            input("Press Enter to continue...")
            break
        else:
            input("Invalid Choice")