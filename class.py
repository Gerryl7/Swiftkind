class myClass:
	def __init__(sample, first,last,age):
		sample.first=first
		sample.last=last
		sample.age=age

	def myFunction(new):
		print("First Name:", new.first)
		print("Last Name:", new.last)
		print("Your Age:", new.age)


firstname=str(input("Enter your First name:"))
lastname=str(input("Enter your Last name:"))
yourage=int(input("Enter your Age:"))

p1=myClass(firstname,lastname,yourage)
p1.myFunction()		

