amount = int(input("Amount: "))
notes_5000 = amount // 5000
amount = amount % 5000
notes_1000 = amount // 1000
amount = amount % 1000
notes_500 = amount // 500
amount = amount % 500
notes_100 = amount // 100
amount = amount % 100
print(f"5000 x {notes_5000}")
print(f"1000 x {notes_1000}")
print(f"500 x {notes_500}")
print(f"100 x {notes_100}")
