
temp=float(input("TEMP:"))
if temp>35:
    print("it is hot day")
print("have a nice day")




bill=int(input("bill amount:"))
if bill>=2000:
    print("free delivery")



num=int(input("a number="))
if  num<0:
    print(-1*(num))



marks=int(input("marks:"))
if marks>=50:
    print("pass")
else:
    print("fail")



bil=float(input("bill amount:  "))
friends=int(input("number of friends:  "))
print("___________________")
print("Service charge: 10%")
a=bil*0.1
print("Service charge amount:",a)
grandtotal=bil+a
print("Grand total:",grandtotal)
print("Each friend has to pay:",grandtotal/friends)





