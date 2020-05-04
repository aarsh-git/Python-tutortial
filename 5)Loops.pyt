#There are 3 types of loops in python- for loop,while loop and nested loop
#Eg:1 while loop
num = 1
while (num <8) :
	print("The no is",num)
	num = num +1
else:
	print("No is greater than 8")
#Eg:2 for loop
list1 = [12,145,1431,42235,76868,5654,111]
for no in list1:
   if no%2 == 0:
      print ("even no is",no)
      
else:
   print ("odd number is",no)

#Eg 3 nested loop-this is a loop in a loop
range(0,5)
for k in range(0,5):
	for i in range(0,k):
		j = i*k
		print(k,end = '')#end='' function space makes the nos appear in a row
		print()#This prints the function in the next line
