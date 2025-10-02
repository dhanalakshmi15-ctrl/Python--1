a = int(input("Enter the number to be check :"))
flag=0
if(a>1):
	for i in range(2,a):
 	 if (a%i == 0):
    		 flag=1
	if(flag==0):
  		print("the number is a prime number")
	else:
 	 print("the enterred number is not a prime number")      
else:
	print("neither prime nor composite")
