# TAKING INPUT YEAR FROM USER
year = input("Enter the year: \n")

# VALIDATING INPUT YEAR
while len(year) != 4 or year.isdigit()!=True:
    year = input('Enter the year again: ')
    
    if len(year) != 4 or year.isdigit()!=True:
        print("\n" + 'Enter a valid year!')

# IF VALID DISPLAY RESULT

if len(year) == 4 or year.isdigit() == True:
    
    result_year = int(year)
    
    if result_year % 4 == 0:
        print(f"\n{result_year} is a leap year!")
        
    elif result_year % 100 == 0:
        print(f"\n{result_year} is a leap year!")

    elif result_year % 400 == 0:
        print(f"\n{result_year} is a leap year!")

    else:
        print(f"\n{result_year} is not a leap year!")
