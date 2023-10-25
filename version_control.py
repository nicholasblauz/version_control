# Nicholas Blauz
def encode(password):
    encoded_password = ""

    for num in password:
        encoded_num = str((int(num) + 3) % 10)
        encoded_password += encoded_num

    return encoded_password
# takes a password of integers and increases each one by 3
# % 10 is used so that if the original integer is 7-10 it is still
# single digit. Ex: 9 becomes 2

def print_menu():
    print(" ")
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    return int(input("Please enter an option: "))
# prints the menu
if __name__ == '__main__':
    encoded_password = ""

    while True:
        option = print_menu()

        if option == 1:
            password = input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored!")
        if option == 2:
            password = input("Please enter your password to decode: ")
            decode(password)
            print(f"The encoded password is {encode(password)}, and the original password is {password}.")
        if option == 3:
            quit()