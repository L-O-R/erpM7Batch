def get_valid(prompt, expected_type = str):
    while True:
        print()
        user_input = input(prompt).strip()

        #input should not be empty
        if not user_input:
            print("Hey! You can't leave this empty")
            continue

        # type check
        try:
            if expected_type == float:
                return float(user_input)
            elif expected_type == int:
                return int(user_input)
            else:
                return user_input
        except ValueError:
            print(f"Error : Please enter a valid {expected_type.__name__}")

# get_valid("Please enter your Name: ", float)

