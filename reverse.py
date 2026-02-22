# reverse_number.py

def reverse_number(num):
    """
    Function to reverse an integer number.
    Handles negative numbers as well.
    """
    sign = -1 if num < 0 else 1
    num = abs(num)

    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return sign * reversed_num


if __name__ == "__main__":
    try:
        number = int(input("Enter an integer: "))
        result = reverse_number(number)
        print("Reversed number:", result)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")