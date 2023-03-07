# Name: Dieuinh Nguyen

def menu():  # Function to display the menu
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")


def encoder(user_password):  # Function to encode password
    encoded_password = ""
    for digit in user_password:
        digit_int = int(digit) + 3  # Add 3 to each digit in password
        digit_str = str(digit_int)  # Turn the new digit into a string
        encoded_password += digit_str
    return encoded_password


def main():
    menu()
    user_choice = int(input("Please enter an option: "))
    encoder_continue = True
    while encoder_continue == True:  # Loop the program until user quits
        if user_choice == 1:  # User enter password to encode
            global global_password  # Create this local variable as a global variable to access outside of scope
            global_password = str(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!\n")
            menu()
            user_choice = int(input("Please enter an option: "))
        elif user_choice == 2:  # Display encoded password
            print(f"The encoded password is {encoder(global_password)}, and the original password is {global_password}.\n")
            menu()
            user_choice = int(input("Please enter an option: "))
        else:
            encoder_continue = False  # Exit the program


if __name__ == "__main__":  # Run the whole program
    main()

