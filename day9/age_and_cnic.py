age = int(input("Age: "))
cnic_input = input("Do you have a CNIC (yes/no): ")
adult = age >= 18
teenager = 13 <= age <= 19
has_cnic = cnic_input == "yes"
can_vote = adult and has_cnic
gets_discount = (age < 12) or (age >= 60)
print("Adult:", adult)
print("Teenager:", teenager)
print("Has CNIC:", has_cnic)
print("Can vote:", can_vote)
print("Gets a discount:", gets_discount)
