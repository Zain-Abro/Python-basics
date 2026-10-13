unitused=int(input("Enter the number of units used: "))
y=unitused
if unitused<=100:
    print("The total cost is: 10 per unit")
elif unitused>100 and unitused<=200:
    print("The total cost is: 15 per unit")
elif unitused>200:
    print("The total cost is: 20 per unit")
print("the bill is :",y*15)