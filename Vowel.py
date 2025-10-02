s=input()
vowels="aeiouAEIOU"
count1=0
count2=0
for i in s:
 if i in vowels:
  print(i)
  count1=count1+1
 else:
  print(i,end="")
  count2=count2+1
print("vowels are",count1)
print("consonanats are",count2)
