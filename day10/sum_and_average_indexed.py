number = int(input("number:"))
total = 0
for i in range(number):
    value = int(input(f"ENTER NUMBERS {i}:"))
    total += value
print(f"The sum is: {total} and the average is:", total / number)
