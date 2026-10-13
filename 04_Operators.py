#arithmetic operators
a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a,b ,sep="#")
print(a**b)



#relational operators
a=50
b=30
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)




#assignment operators
a=150
b=100

a+=10
print(a)
a-=4
print(a)
b*=2
print(b)



#logical operators
a=True
b=False
print(a and b)
print(a or b)
print(not a)

#
print(17//5)
print(17%5)
print(2**4 )
print(10/5)
bill=float(input("enter the bill amount:"))
friends=int(input("total number of friends:"))
print("----------------------")
print("service (10%):", bill * 0.1)
print("grand total:",bill + (bill * 0.1))
print("each friend pays:", (bill + (bill * 0.1))/friends)
a=10
b=5
temp=a
b=a
b=temp
print("a is ",a)
print("=" * 30)