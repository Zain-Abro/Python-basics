name = input("enter your name:")
count = 0
for letter in name:
    print(letter, end="")
    count += 1
print()
print("number words in name:", count)
