'''
Program to find factorial of a number!
'''
number = int(input("Enter a number: "))

result = 1

while number >= 1:
    result = result * number
    number -= 1

print(f"Factorial = {result}")
