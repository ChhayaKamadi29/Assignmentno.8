#Write a program find reverse of a number
def reverse_number(num):
    is_negative = num < 0
    num = abs(num)
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10

    return -reversed_num if is_negative else reversed_num

number = int(input("Enter a number: "))

result = reverse_number(number)

print(f"The reverse of {number} is: {result}")