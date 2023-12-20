# Programme to find compound interest for a given principal, time and roi

def main():
    pri = get_posint("Enter the principal amount: ")
    time = get_posint("Enter the time in months: ")
    years = time_year(time)
    roi = get_float("Enter the roi: ")
    result = cmpnd_intrst(pri, years, roi)
    print(f"The compound interest for the given principal {
          pri} after {time} months for roi {roi} is: {result}")


def get_posint(prompt):
    """Function to get the positive integers from users"""
    while True:
        try:
            x = int(input(prompt))
            if x > 0:
                return x
            else:
                print(f"Enter positive integers only")
        except ValueError:
            print(f"Enter integers only")


def time_year(time):
    """Function to convert months into years"""
    return (time // 12)


def get_float(prompt):
    """Function to get the floating point number from a user"""
    while True:
        try:
            x = float(input(prompt))
            if x > 0:
                return x
            else:
                print(f"Enter positive floats only")
        except ValueError:
            print(f"Enter floats only")


def cmpnd_intrst(pri, time, roi):
    """Function for finding the compound interest"""
    return pri*((1 + (roi / 100)) ** time)


if __name__ == "__main__":
    main()
