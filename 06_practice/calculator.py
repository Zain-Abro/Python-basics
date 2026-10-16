num1=int(input("Number1: "))
num2=int(input("Number2: "))
op=input("Enter operator (+,-,*,/):")
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    if num2==0:
        print("division error")
    else:
        print(num1/num2)
