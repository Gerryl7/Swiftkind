#class MyClass:
 # x = 40

#print(MyClass().x)

#CLASS init function
"""
class Person:
  def __init__(self, name, age,sex):
    self.name = name
    self.age = age
    self.sex = sex

p1 = Person("John", 36, "male")

print(p1.name)
print(p1.age)
print(p1.sex)"""

# Call back the Function and CLASS
'''
class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def myfunction(self):
		print("name is" +self.name)

pl=person("Gerryl", 19)
pl.myfunction() # Print the Class'''

#NOT SELF
'''
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()'''

'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
print(p1.age)
p1.age = 40
#del p1.age # this can delete the AGE #it can also delte the whole P1 through "del p1"

print(p1.age)
'''
'''
class Gerryl:
  def __init__(self, name):
    self.name = name

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Gerryl("Gerryl")
p1.myfunc()
print(p1.name)


class Lozarita:
  def __init__(self, middle):
    self.middle = middle

  def myfunc(abc):
    print("Hello my Middle name is " + abc.middle)

p1 = Lozarita("Gerryl")
p1.myfunc()
print(p1.middle)


class Destor:
  def __init__(self, surname):
    self.surname = surname

  def myfunc(abc):
    print("Hello my Last name is " + abc.surname)

p1 = Destor("Destor")
p1.myfunc()

print(p1.surname)'''
#CaLL CLASS IN OTHER  CLASS

'''
class myclass:
	def __init__(name,middle,surname,age):
		name.age=age
		name.middle=middle
		name.surname=surname

	def myfucntion(fun):
		print(fun.age)
		print(fun.middle)
		print(fun.surname)

p1=myclass("Lozarita","Destor",19)
p1.myfucntion()


class newclass:
	p1=myclass("Lozaasarita","Desasastor",129)
	p1.myfucntion()
'''
'''
#What is your SYSTEM????
import platform
x = platform.system()
print(x)
'''

'''def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}'''

#Time this day
'''import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%D"))
'''
#CamelCase
'''import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))
'''

'''import tkinter 
top = tkinter.Tk()
# Code to add widgets will go here...

top.mainloop()'''

#Paragraph
'''
paragraph = """This is a paragraph. It is
made up of multiple      lines and sentences."""

print (paragraph)
'''

