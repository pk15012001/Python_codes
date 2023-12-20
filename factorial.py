# Programme to find the factorial of a given number

def main():
    num = get_posint("Enter the number: ")
    result = fact_num(num)
    print(f"The factorial of the given number is: {result}")


def get_posint(prompt):
    """Function to get positive integers from user"""
    while True:
        try:
            x = int(input(prompt))
            if x > 0:
                return x
            else:
                print(f"Enter positive integers only")
        except ValueError:
            print(f"Enter integers only")


def fact_num(num):
    """Function to get the factorial of a given number"""
    if num == 0:
        return 1
    else:
        return (num * fact_num(num - 1))


if __name__ == "__main__":
    main()
