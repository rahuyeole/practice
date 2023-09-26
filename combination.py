#decimal to octal
def decimal_to_octal(decimal_num):
    octal_num = oct(decimal_num)[2:] 
    return octal_num

decimal_num = int(input("Enter a decimal number: "))
octal_num = decimal_to_octal(decimal_num)
print(f"The octal representation of {decimal_num} is {octal_num}")

#Reverse an iNteger
def reverse_integer(num):
    reversed_num = int(str(num)[::-1])
    return reversed_num

num = int(input("Enter an integer: "))
reversed_num = reverse_integer(num)
print(f"The reversed integer is {reversed_num}")

#Fibonacci Reversive Method ._.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.-.-..-.-.-.-.-
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci_recursive(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

n = int(input("Enter the number of Fibonacci terms to generate: "))
fib_series = fibonacci_recursive(n)
print(f"The Fibonacci series is: {fib_series}")

#Return nth value from fibonaci series
def fibonacci_nth_value(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

n = int(input("Enter the value of N to get the Nth Fibonacci number: "))
nth_value = fibonacci_nth_value(n)
if nth_value is not None:
    print(f"The {n}th value in the Fibonacci sequence is {nth_value}")
else:
    print("Invalid input for N.")

