words=["Always","Create","Believe","That","Something","Love","Wonderful","Is","About","Live","To","Happen","Exit"]

y=0
for x in words:
	if(x=="Create"):
		del words[y]
		y+=1
	elif(x=="Love"):
		del words[y]
		y+=1
	elif(x=="Live"):
		del words[y]
		y+=1
	elif(x=="Exit"):
		del words[y]
		y+=1
	
	else:
		y+=1

print(words)
del words 
print("all words taht you read is deleted: \n")
words=["",""]

wordscount=0
choice=str(input("Do you want to Enter Words? y/n:  "))

if(choice=="y"or"Y"):
	choice2="y"
	while(choice2=="y"):
		app=str(input("Enter word to Append:  "))
		words.append(app)
		wordscount+=1
		choice2=str(input("Do you want to Enter Words? y/n:  "))


	
	else:
		print("Your Words are:")
		for x in words:
			print(x)
