sentence = input("sentence:")
count = 0
for character in sentence:
    if character in "aeiouAEIOU":
        count += 1
print("number of vowels present in sentence are:", count)
