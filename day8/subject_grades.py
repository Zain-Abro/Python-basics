maths = int(input("enter maths marks:"))
eng = int(input("enter eng marks:"))
sci = int(input("enter science marks:"))
print("MATH:", maths)
print("ENGLISH:", eng)
print("SCIENCE:", sci)
print("-" * 20)
total = maths + eng + sci
percentage = (total / 300) * 100
print(f"total : {total}/300")
print("Percentage:", percentage)
if maths >= 40 and eng >= 40 and sci >= 40:
    if percentage > 80:
        print("GRADE :A")
    elif percentage > 60:
        print("GRADE: B")
    elif percentage > 50:
        print("GRADE : C")
    else:
        print("GRADE: F")
else:
    print("Result: FAIL")
