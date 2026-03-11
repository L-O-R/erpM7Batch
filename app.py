import sys

from Assets import Hardware, Asset, Software
from AssetsMenu import manage_assets
from CompanyFinancial import manage_financials
from Employees import Manager, Employee
from EmployessMenu import manage_employees

def save_data(emp_dict, asset_dict):
    try:
        with open("employees.txt", "w") as file:
            for emp in emp_dict.values():
                if emp.role == "Manager":
                    line = f"{emp.emp_id}|{emp.name}|{emp.role}|{emp.salary}|{emp.bonus}"
                else:
                    line = f"{emp.emp_id}|{emp.name}|{emp.role}|{emp.salary}"
                file.write(line + '\n')

        with open("assets.txt", "w") as file:
            for asset in asset_dict.values():
                line = f"{asset.asset_id}|{asset.name}|{asset.value}"

                if isinstance(asset, Hardware):
                    line += f"|Hardware|{asset.condition}"
                else:
                    line += f"|Software|{asset.expiry_date}"
                file.write(line + '\n')
    except Exception as e:
        print(f" Critical Error During Save: {e}")


def load_data():
    employees = {}
    assets = {}
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                data = line.strip().split('|')
                # print(data)
                if data[2] == "Manager":
                    emp = Manager(data[0], data[1],data[2], float(data[3]) , float(data[4]))
                else:
                    emp = Employee(data[0], data[1],data[2], float(data[3]))
                employees[data[0]] = emp

        with open("assets.txt", "r") as file:
            for line in file:
                data = line.strip().split('|')
                if data[3] == "Hardware":
                    asset = Hardware(data[0], data[1], float(data[2]), data[4])
                else:
                    asset = Software(data[0], data[1], float(data[3]), data[4])
    except FileNotFoundError:
        print(f" NO Previous Data Found. Starting Fresh")
    return employees, assets



def run_system():
    # 1. The Storage
    # Using Dictionary
    (employees, assets) = load_data()
    asset_ids = set()

    ADMIN_USER = "admin"
    ADMIN_PASS = "1234"

    print("=" * 50)
    print("            Welcome to NexGen Erp")
    print("=" * 50)

    attempts = 0
    authenticated = False
    while attempts < 3:
        user = input("Please enter your username: ").strip()
        password = input("Please enter your password: ").strip()
        if user == ADMIN_USER and password == ADMIN_PASS:
            print("\n Access Granted. Welcome to NexGen Erp")
            print("=" * 50)
            authenticated = True
            break
        else:
            attempts += 1
            print("=" * 50)
            print(" Login Failed, Check your username and password")
    if not authenticated:
        print("=" * 50)
        print("Too Many attempts . Closing System .......")
        sys.exit()

    while True:
        print("=" * 50)
        print("          Main Menu")
        print("=" * 50)
        print("1. Manage Employees")
        print("2. Mange Assets")
        print("3. Company Financials")
        print("4. Save Data")
        print("5. Exit System")

        choice = input("Please enter your choice: ").strip()
        if choice == "1":
            print("------ Employee Management Loading.....")
            print()
            manage_employees(employees)
            input("Please Press Enter to Continue").strip()
        elif choice == "2":
            print("------ Asset Management Loading.....")
            print()
            manage_assets(assets, employees, asset_ids)
            input("Please Press Enter to Continue").strip()
        elif choice == "3":
            print("------ Company Financial Loading.....")
            print()
            manage_financials(employees, assets)
            input("Please Press Enter to Continue")
        elif choice == "4":
            # print("------ Save & exit")
            save_data(employees, assets)
            print("Data Saved Successfully")
            input("Please Press Enter to Continue").strip()
        elif choice == "5":
            print("------ Exit System")
            sys.exit()
        else:
            print("Please enter a valid choice 1 to 4 only in numeric form")

run_system()