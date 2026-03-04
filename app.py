import sys

def run_system():
    # 1. The Storage
    # Using Dictionary
    employees = {}
    assets ={}
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
        print("4. Save & exit")

        choice = input("Please enter your choice: ").strip()
        if choice == "1":
            print("------ Employee Management Loading.....")
        elif choice == "2":
            print("------ Asset Management Loading.....")
        elif choice == "3":
            print("------ Company Financial Loading.....")
        elif choice == "4":
            print("------ Save & exit")
            break
        else:
            print("Please enter a valid choice 1 to 4 only in numeric form")














run_system()