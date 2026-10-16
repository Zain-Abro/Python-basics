

letter = input("Enter a letter: ")
if letter in "asvmsadjsbad":
    print("letter is present")
else:
    print("letter is not present")




letter = "e"
if letter in "aeiou":
    print("vowel")

answer = input("coninue? (yes or no): ")
if answer=="yes" or answer=="Yes":
    print("continue")
elif answer=="no" or answer=="NO" :
    print("stopped")
else:
    print("please answer (yes or no)")


email=input("enter your email:")
if "@" in email and "." in email and " " not in email :
    print("valid email")
else:
    print("invalid email")
