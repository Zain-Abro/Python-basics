email = input("enter your email:")
if "@" in email and "." in email and " " not in email:
    print("valid email")
else:
    print("invalid email")
