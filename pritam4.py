import random

d=0
p=0

while True:
	r = input("Press r to roll,q to quit:")

	if r =='r':
		d = random.randint(1,6)
		print("you got:",d)
		if d == 6:
			print("congratulation, you can start the game now")
			break
		else:
			print("roll again,till you get 6.")

while True:
	r = input("Press r to roll, q to quit:")

	if r == 'r':
		d = random.randint(1,6)
		print("you got:",d)

		p= p+d
		if p >100:
			p=p-d
			print("wait till you get",100-p)

		print("your new position is:",p)

		if p == 100:
			print("you won!")
			exit()
		if p == 8:
			p = 37
			print("wow, a ladder. Go to",p)
		if p == 11:
			p = 2
			print("sad, a snake. Go to",p)
		if p == 13:
			p = 34
			print("wow, a ladder. Go to",p)
		if p == 25:
			p = 4
			print("sad, a snake. Go to",p)
		if p == 38:
			p = 9
			print("sad, a snake. Go to",p)
		if p == 40:
			p = 68
			print("wow, a ladder. Go to",p)
		if p == 52:
			p = 81
			print("wow, a ladder. Go to",p)
		if p == 65:
			p = 46
			print("sad, a snake. Go to",p)
		if p == 76:
			p = 97
			print("wow, a ladder. Go to",p)
		if p == 89:
			p = 70
			print("sad, a snake. Go to",p)
		if p == 93:
			p = 64
			print("sad, a shnake. Go to",p)

	elif r == 'q':
	    print("bye!")
	    exit()