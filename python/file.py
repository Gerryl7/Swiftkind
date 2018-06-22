'''f = open("demotxt.txt", "w")

print(f.read()) #it can be 1print(f.read(5)) ::output "Hello"
'''
'''
f = open("demotxt.txt", "r")

print(f.readline(23))'''

#looping text line
'''f = open("demotxt.txt", "r")
y=0
for x in f:
	if(y==1):
		print(x)
		break
	y+=1'''
'''
f = open("demotxt.txt", "a") # Append to a File
f.write("dfdfdfdfd") #Rewrite all files "w" , but this will write to a file

f = open("myfile.txt", "x") #Create a File "x"
'''

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exists")

  #os.rmdir() Remopve Folder
  #os.remove() Remove Txt file