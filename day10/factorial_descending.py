factorial = 1
number = int(input("enter number:"))
if number == 0:
    print("factorial of 0! is = 1")
else:
    for i in range(number, 0, -1):
        factorial *= i
    print(f"{factorial} is the factorial of {number}")
