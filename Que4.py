#Sum of all odd numbers between 1 to n

def sum_of_odd_numbers(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total


n = int(input("Enter the value of n: "))
print(f"The sum of all odd numbers between 1 and {n} is: {sum_of_odd_numbers(n)}")