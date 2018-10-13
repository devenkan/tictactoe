import random
import time

list=[0,1,2,3,4,5,6,7,8]


def check(c,p1,p2,p3):
	if list[p1]==c and list[p2]==c and list[p3]==c:
		return "win"




def check1(c):
	if check(c,0,1,2)=="win":
		return "win"
	elif check(c,3,4,5)=="win":
		return "win"
	elif check(c,6,7,8)=="win":
		return"win"
	elif check(c,0,3,6)=="win":
		return"win"		
	elif check(c,1,4,7)=="win":
		return"win"
	elif check(c,2,5,8)=="win":
		return"win"	
	elif check(c,0,4,8)=="win":
		return"win"
	elif check(c,3,4,5)=="win":
		return"win"	
	elif check(c,2,4,6)=="win":
		return"win"				




def show():
	print("---------")
	print(list[0],"|",list[1],"|",list[2])
	print("---------")
	print(list[3],"|",list[4],"|",list[5])
	print("---------")
	print(list[6],"|",list[7],"|",list[8])
	print("---------")


while True:
	choice=input("enter the  position")
	choice=int(choice)
	if list[choice]!="X" and list[choice]!="Y":
		list[choice]="X"
		if check1('X')=='win':
			show()
			print("user win")
			break
		finding=True
		while finding:
			computerinput=random.randint(0,8)
			if list[computerinput]!="Y" and list[computerinput]!="X":
				list[computerinput]="Y"
				finding=False
				if check1('Y')=="win":
					finding=False
					show()
					print("computerinput win")
					break

	else:
		print("the number is already reserved")	

		
	show()	
show()