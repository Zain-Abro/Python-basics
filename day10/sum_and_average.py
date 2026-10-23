number = int(input("number:"))
total = 0
for i in range(1, number + 1):
    values = int(input("values:"))
    total += values
print(total)
average = total / number
print(average)
