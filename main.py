number = int(input("Enter a number: "))

flag = 1

for n in range(2, number):
    if (number % n == 0):
        flag = 0
        break

if (flag==1):
    print(f"{number} is prime!")

elif (flag==0):
    print(f"{number} is non-prime!")