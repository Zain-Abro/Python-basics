number = int(input("enter:"))
largest = number
for i in range(2, 6):
    number = int(input(f"enter {i}:"))
    if number > largest:
        largest = number
print("largest number is", largest)
