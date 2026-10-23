num = int(input("Enter the any number:"))
count = 0
for i in range(1, num + 1):
    value = int(input(f"Enter {num} values {i}:"))
    if value > 0:
        count += 1
print("Total Positive value:", count)
