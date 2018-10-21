import tkinter as tk
from tkinter import simpledialog
#1
def yeet():
	yeet=[1, 5, 355,65]
	lit = [yeet[0],yeet[-1]]
	print (lit)
yeet();
#2
ab = [1,0,2,-4,3,6,25,87]
ba = []
def ab1(ab):
	for i in range(len(ab)):
		if ab[i]< 5:
			ba.append(ab[i])
	return ba
print(ab1(ab))
#3
pic = [1,2,3,4,5,4,67,89,99]
tic = [1,4,3,67,88,77,5,100]
nic = []
def top():
	for i in pic:
		if i in tic:
			if  i in nic:
				pass
			else:
				nic.append(i)
	print (nic)
top()
#4
quastion = simpledialog.askstring("Input", "GIVE A NUMBER!", parent=tk.Tk())
def is_prime(number):
	for i in range(2,number):
		if number % i == 0 :
			return(False)
	return (True)
answer = simpledialog.askstring("Input","is_prime", parent=tk.Tk())
x= is_prime(6)	
print(x)
# input("give a number")