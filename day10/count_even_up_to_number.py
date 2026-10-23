num = int(input("Enter the any Number:"))
count = 0
for i in range(1, num + 1):
    if i % 2 == 0:
        count += 1
print(count)
