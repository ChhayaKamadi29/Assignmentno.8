#Write a program to find print the following Fibonacci series using functions: 1 1 2 3 5 8 n terms
def print_fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return

    a, b = 1, 1

    print(f"Fibonacci series ({n} terms):")
    for i in range(n):
        print(a, end=" ")
        # Update terms: next term is the sum of previous two
        a, b = b, a + b
    print()

terms = int(input("Enter number of terms (n): "))

print_fibonacci(terms)