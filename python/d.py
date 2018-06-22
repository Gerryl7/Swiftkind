# IF/ ELSE 
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

  #While Loop
  i = 1
while i < 6:
  print(i)
  if i == 3:
    break #It can be "CONTINUE"
  i += 1

 #FOR LOOP
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#-----------------
for x in range(6):
  print(x)
  #---------------
  for x in range(2, 6):
  	print(x)
  #---------RECURSION
  for x in range(2, 30, 3):
   	print(x)

  #FUNCTION def means defined
def my_function(country = "Norway"):
	print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Function using Return Statement
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#LAMBDA Like Function, has return, Applicable only for String
def myfunc(n):
  return lambda i: i*n

doubler = myfunc(2)
tripler = myfunc(3)
val = 11
print("Doubled: " + str(doubler(val)) + ". Tripled: " + str(tripler(val)))

#ARRAY OR LIST
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#Fucntion thislist.APPEND("")
#Fucntion thislist.REMOVE("")
# FIND THE LENGTH print(len(thislist))
#sort()
#reverse()
#pop()
# add in specific position // insert()
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#index()	Returns the index of the first element with the specified value

#CLASS
class MyClass:
  x = 5

print(MyClass)


#MY
cars = ["Ford", "Volvo", "BMW"]
y=1
for x in cars:
	if (x=="Volvo"):
	 	cars.pop(y)
y+=1
print(cars)


