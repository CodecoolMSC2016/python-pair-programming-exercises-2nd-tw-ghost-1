def palindrome(text):
    return

def main():
    text = input("Type: ")
    textwithoutspaces = text.replace(" ", "")
    if str(textwithoutspaces.lower()) == str(textwithoutspaces.lower())[::-1]:
        print("True")
    else:
        print("False")
    return


if __name__ == '__main__':
    main()
