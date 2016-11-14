def main():
    for loop in range(1,101):
        print(loop)
        if loop % 15 == 0:
            print ("FizzBuzz")
        elif loop % 5 == 0:
            print ("Buzz")
        elif loop % 3 == 0:
            print ("Fizz")
        else:
            print("Normal")

    return

if __name__ == '__main__':
    main()


