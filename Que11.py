#WAP to check if a given number is Armstrong number or not. For each task create separate functions.
def count_digits(num):
    if num == 0:
        return 1
    count = 0
    temp = abs(num)
    while temp > 0:
        count += 1
        temp //= 10
    return count


def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result


def calculate_armstrong_sum(num):
    num_of_digits = count_digits(num)
    total_sum = 0
    temp = abs(num)

    while temp > 0:
        digit = temp % 10
        total_sum += power(digit, num_of_digits)
        temp //= 10

    return total_sum


def is_armstrong(num):
    if num < 0:
        return False
    return num == calculate_armstrong_sum(num)

number = int(input("Enter a number: "))

if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")