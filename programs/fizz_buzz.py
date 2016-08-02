# A program takes the input from the user and generates the range of number between 1 to entered number and process further as below 
# If the number is mod of 3 and 5 then prints 'fizz buzz'
# Else If the number is mod of 5 then prints buzz
# Else If the number is mod of 3 then prints fizz

a=input("Enter the number: \n")
r_number = range(1,a+1)
print "\nTotal numbers generated:\t", r_number
for i in r_number:
	if i%3==0 and i%5==0:
		print i,': ','fizz buzz'
	elif i%5==0:
		print i,': ','buzz'
	elif i%3==0:
		print i,': ','fizz'
