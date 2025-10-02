a=int(input("enter the first number a:"))
b=int(input("enter the second number b:"))
a=a-b
b=a+b
a=b-a
print("after swapping a :",a)
print("after swapping b :",b)


temp=a
a=b
b=temp
