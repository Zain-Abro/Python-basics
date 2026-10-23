bill = float(input("bill amount:  "))
friends = int(input("number of friends:  "))
print("___________________")
print("Service charge: 10%")
service_charge = bill * 0.1
print("Service charge amount:", service_charge)
grand_total = bill + service_charge
print("Grand total:", grand_total)
print("Each friend has to pay:", grand_total / friends)
