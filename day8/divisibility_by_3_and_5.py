number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by both 3 and 5.")
elif number % 3 == 0:
    print(f"{number} is divisible by 3, but not by 5.")
elif number % 5 == 0:
    print(f"{number} is divisible by 5, but not by 3.")
else:
    print(f"{number} is not divisible by 3 or 5.")
