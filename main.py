def encode(dec_password):
    dec_password_list = []
    password_list = []
    for i in dec_password:
        dec_password_list.append(int(i))
    for i in dec_password_list:
        password_list.append((i + 3) % 10)
    # print(*password_list, sep="")
    encoded_password = "".join(map(str, password_list))
    return encoded_password


def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n ")

if __name__ == '__main__':
    start = True
    choice = ""
    while start:
        menu()
        choice = int(input("Please enter an option: "))
        if choice == 1:
            dec_password = input("Please enter your password to encode: ")
            new = encode(dec_password)
            print("Your password has been encoded and stored!")

        if choice == 2:
            print(f"The encoded password is {encode(dec_password)}, and the original password is {dec_password}.")

        if choice == 3:
            start = False



