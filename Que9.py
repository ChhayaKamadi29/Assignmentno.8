#Write a program to check if entered number is a palindrome or not.
def is_palindrome(num):
    if num < 0:
        return False

    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10

    return original_num == reversed_num

number = int(input("Enter a number: "))

if is_palindrome(number):
    print(f"{number} is a palindrome number.")
else:
    print(f"{number} is not a palindrome number.")