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

# Name: David Fackson
def decoder(encoded_password):
    new_password = ''
    for i in range(len(encoded_password)):
        if encoded_password[i] == '0':
            new_password = new_password + '7'
        elif encoded_password[i] == '1':
            new_password = new_password + '8'
        elif encoded_password[i] == '2':
            new_password = new_password + '9'
        elif encoded_password[i] == '3':
            new_password = new_password + '0'
        elif encoded_password[i] == '4':
            new_password = new_password + '1'
        elif encoded_password[i] == '5':
            new_password = new_password + '2'
        elif encoded_password[i] == '6':
            new_password = new_password + '3'
        elif encoded_password[i] == '7':
            new_password = new_password + '4'
        elif encoded_password[i] == '8':
            new_password = new_password + '5'
        elif encoded_password[i] == '9':
            new_password = new_password + '6'
    return new_password

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
            print(f"The encoded password is {encoder(global_password)}, and the original password is {decoder(encoded_password)}.\n")
            menu()
            user_choice = int(input("Please enter an option: "))
        else:
            encoder_continue = False  # Exit the program


if __name__ == "__main__":  # Run the whole program
    main()

