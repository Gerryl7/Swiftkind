print("Simple Calculator:")
print("A: Addition")
print("B. Subtraction")
print("C. Multiplication:")
print("D. Division")

answer=str(input("Select One:"))
number1=int(input("First to Calculate:"))
number2=int(input("Second to Calculate:"))

try:
	if(answer=="A"or "a"):
		print("Addition: ",number1+number2)

	elif(answer=="B"or"b"):
		print("Subtraction: ",number1-number2)
	
	elif(answer=="C"or"c"):
		print("Multiplication: ",number1*number2)
	
	elif(answer=="D"or"d"):
		print("Division: ",number1/number2)
	
	else:
		print("Wrong Choice!")
		
except ValueError:
        print("Oops!  That was no valid number.  Try again...")


