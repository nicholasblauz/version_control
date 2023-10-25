# Nicholas Blauz - Encode
# Danush Singla - Decode
def encode(password):
    encoded_password = ""

    for num in password:
        encoded_num = str((int(num) + 3) % 10)
        encoded_password += encoded_num

    return encoded_password
# takes a password of integers and increases each one by 3
# % 10 is used so that if the original integer is 7-10 it is still
# single digit. Ex: 9 becomes 2

def decode(password):               # decodes the password
    decoded_password = ""

    for character in password:      # goes through each character in the password string
        if int(character) <= 2:
            character = (int(character) -  3) + 10        # adds 10 to wrap the value around
            decoded_password += str(character)           # converts the character back into a string
        else:
            decoded_password += str(int(character) - 3)     # subtracts three to the character and returns as a string

    return decoded_password

def print_menu():
    print(" ")
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")

    return int(input("Please enter an option: "))
# prints the menu
if __name__ == '__main__':
    encoded_password = ""

    while True:
        option = print_menu()

        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print("")
        if option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            print("")
        if option == 3:
            quit()