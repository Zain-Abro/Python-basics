# Ask the user for the amount
amount = int(input("Amount: "))

# Calculate the number of 5000 notes and update the remaining amount
notes_5000 = amount // 5000
amount = amount % 5000

# Calculate the number of 1000 notes and update the remaining amount
notes_1000 = amount // 1000
amount = amount % 1000

# Calculate the number of 500 notes and update the remaining amount
notes_500 = amount // 500
amount = amount % 500

# Calculate the number of 100 notes
notes_100 = amount // 100
amount = amount % 100

# Print the results using f-strings for formatting
print(f"5000 x {notes_5000}")
print(f"1000 x {notes_1000}")
print(f"500 x {notes_500}")
print(f"100 x {notes_100}")