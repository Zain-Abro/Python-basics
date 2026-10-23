n = int(input("Enter N numbers:"))
value = int(input("Enter value:"))
small = value
large = value
for i in range(1, n + 1):
    num = int(input(f"Enter the Numbers {i}:"))
    if num < small:
        small = num
    if num > large:
        large = num
print("Smallest Value:", small)
print("Largest Value:", large)
