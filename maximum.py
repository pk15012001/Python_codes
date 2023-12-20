# Programme to find the largest among the given three numbers

def main():
    num1 = get_num("Enter the first number: ")
    num2 = get_num("Enter the second number: ")
    num3 = get_num("Enter the third number: ")
    result = largest_num(num1, num2, num3)
    print(f"The largest among the given three numbers is: {result}")


def get_num(prompt):
    """Function to get the proper numbers from users"""
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print(f"Enter numbers only")


def largest_num(num1, num2, num3):
    """Function to get the largest among the given three numbers"""
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3


if __name__ == "__main__":
    main()
