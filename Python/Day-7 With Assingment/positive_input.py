class NegativeNumberError(Exception):
    pass

while True:
    try:
        n = int(input("Enter a positive number: "))

        if n < 0:
            raise NegativeNumberError

        print("Valid Number =", n)
        break

    except ValueError:
        print("Enter integers only!")

    except NegativeNumberError:
        print("Negative number not allowed!")