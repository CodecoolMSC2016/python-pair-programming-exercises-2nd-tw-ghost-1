import random
def passwordgen():
    return

def main():
    while True:
        choice = input("Do you want a badass password?: ")
        if choice == "yes":
            alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            pw_length = 8
            mypw = ""

            for i in range(pw_length):
                next_index = random.randrange(len(alphabet))
                mypw = mypw + alphabet[next_index]
            print()
            print(mypw)
        elif choice == "no":
            print("Goodbye!")
            break
        else:
            print()
            print("Please type a valid answer.")

    return


if __name__ == '__main__':
    main()
