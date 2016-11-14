import datetime


def years(age):
    return


def main():
    name = str(input("Type your entire name: "))
    age = int(input("Type your age: "))
    now = datetime.datetime.now()
    yearofhundred = now.year - age + 100
    print("Dear {}, ".format(name))
    print("you will be 100 years old in {}".format(yearofhundred))
    return


if __name__ == '__main__':
    main()