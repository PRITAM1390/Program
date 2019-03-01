import random
l=["r","p","s"]
us=0
cs=0
while True:
	#take input from user
	u=input("enter your choice,press n to discontinue")
	#to exit
	if u=='n':
		print("Game Over")
		print("user score is",us)
		print("computer score is",cs)		
		exit()
		if cs>us:
			print("computer is winner")
		else:
			print("user is winner")
	#input from computer
	c=random.choice(l)
	print("computer chooses",c)

	#compare the user and computer choice
	if u==c:
		print("tie")
	elif u=="r" and c=="p":
		cs=cs+1
		print("comp wins")
	elif u=="p" and c=="r":
		us=us+1
		print("user wins")
	elif u=="p" and c=="s":
		cs=cs+1
		print("comp wins")
	elif u=="s" and c=="p":
		cs=cs+1
		print("user wins")	
	elif u=="r" and c=="s":
		us=us+1
		print("user wins")
	elif u=="s" and c=="r":
		cs=cs+1
		print("comp wins")
