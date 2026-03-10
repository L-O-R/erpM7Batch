from Assets import Hardware, Software
from Employees import Employee
from Validator import get_valid


def manage_assets(assets_dict, employee_dict, asset_ids_set):
    while True:
        print("=" * 50)
        print("          Asset Management Menu")
        print("=" * 50)
        print()
        print("Select an option to continue:")
        print()
        print("1. Add Assets")
        print("2. View All Assets")
        print("3. Assign Assets")
        print("4. Calculate Deprecation")
        print("5. Back to Main Menu")
        print()
        print("_" * 50)

        choice = input("Select an option: ")
        if choice == "1":
            while True:
                a_type = get_valid("Asset Type (Hardware/Software): ").capitalize()
                if a_type not in ['Hardware', 'Software']:
                    print("Invalid Asset Type")
                    continue
                else:
                    break
            name = get_valid("Asset Name: ", str)
            value = get_valid("Asset Value: ", float)

            if not assets_dict:
                new_id = "A101"
                # E101 => 101
            else:
                last_id = max(int(eid[1:]) for eid in assets_dict.keys() )
                new_id = f"A{last_id + 1}"

            if a_type == "Hardware":
                cond = get_valid("Physical Condition: ").capitalize()
                new_assets = Hardware(new_id, name, value, cond)
            else:
                exp_date = get_valid("Expiration Date: ").capitalize()
                new_assets = Software(new_id, name, value, exp_date)
            assets_dict[new_id] = new_assets
            print(f"Asset {new_id} added")
        elif choice == "2":
            if not assets_dict:
                print("No Asset Found")
                continue

            for asset in assets_dict.values():
                print(asset.get_details())
                print('-' * 60)
            print()
            input("Press Enter to Continue...")
        elif choice == "3":
            if not assets_dict:
                print("No Asset Found")
                continue

            if not employee_dict:
                print("No Employee Found")
                continue

            e_id = get_valid("Enter Employee Id to Assign Assets: ")

            if e_id not in employee_dict.keys():
                print("Invalid Employee Id")
                continue

            a_id = get_valid("Enter Asset Id to Assign: ")

            if a_id not in assets_dict.keys():
                print("Invalid Asset Id")


            asset_data = assets_dict[a_id]
            emp_data = employee_dict[e_id]

            emp_data.assign_assets(asset_data)
            print(f"Asset {a_id} assigned  to {emp_data.name}")
            employee_dict[e_id] = emp_data





