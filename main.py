# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def encode(password):
    encoded_pass = ""
    for i in password:
        i = int(i)
        t = i + 1
        u = str(t)
        encoded_pass += u
    return encoded_pass
def decode(password):
    decodedword = ""
    for i in password:
        i = int (i)
        p = i - 3
        o = str(p)
        decodedword += o

    return decodedword





def main():
    encoded = None

    while True:
        print("Menu")
        print("--------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        menu_selection = int(input("please enter an option: "))
        if menu_selection == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)

        elif menu_selection ==2:
            decoded = decode(encoded)
            print("The encoded password is " + encoded + "and the orginal password is " + decoded + ".")
        elif menu_selection ==3:
            break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


