value = 0
for i in range(1, 6):
    num = int(input(f"Enter Values {i}:"))
    if value == 0 or num > value:
        value = num
print("Largest Num:", value)
