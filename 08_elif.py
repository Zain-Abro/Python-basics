maths=int(input("enter maths marks:"))
eng=int(input("enter eng marks:"))
sci=int(input("enter science marks:"))
print("MATH:",(maths))
print("ENGLISH:",(eng))
print("SCIENCE:",(sci))
print("-"*20)
a = maths + eng+ sci
percentage =(a/300)*100
print(f"total : {a}/300")
print("Percentage:",percentage)

if maths>=40 and eng>=40 and sci>=40:
    if percentage>80:
        print("GRADE :A")
    elif percentage>60:
        print("GRADE: B")
    elif percentage>50:
        print("GRADE : C")
    else:
        print("GRADE: F")
else:
    print("Result: FAIL")

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by both 3 and 5.")
elif number % 3 == 0:
    print(f"{number} is divisible by 3, but not by 5.")
elif number % 5 == 0:
    print(f"{number} is divisible by 5, but not by 3.")
else:
    print(f"{number} is not divisible by 3 or 5.")
