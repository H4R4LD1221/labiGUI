#!/usr/bin/python3
import os
import lybe
import sys
import signal
import time
from tkinter import *

root = Tk()

root.title("Labyrinthe")
root.geometry("450x700")
root.configure(background='black')

def ex():
	exit(0)
def restart(event):
	with open("map_or.txt","r") as mr:
		with open("map.txt",'w') as m:
			for e in mr:
				m.write(e)
	Main()			
def men():
	menu = Menu(root)
	root.config(menu=menu)
	submenu = Menu(menu)
	menu.add_cascade(label="Game",menu = submenu)
	submenu.add_command(label="Restart",command=restart)
	submenu.add_command(label="Exit",command=ex)

def exo(signal,frame):
	print("\nGame is closing")
	time.sleep(1)
	print("Good bye!")
	sys.exit(0)

def Main():
	def up(event):
		backup = sys.stdout
		lybe.Some("X","O").up()
		sys.stdout = backup
		runner()
	def down(event):    
		backup = sys.stdout
		lybe.Some("X","O").down()
		sys.stdout = backup
		runner()
	def left(event):			
		backup = sys.stdout
		lybe.Some("X","O").left()
		sys.stdout = backup
		runner()	
	def right(event):	
		backup = sys.stdout
		lybe.Some("X","O").right()
		sys.stdout = backup
		runner()	
	signal.signal(signal.SIGINT,exo)
	hu = open("map.txt","r")
	lop = 0
	for huhu in hu:
		for hi in range(len(huhu)):
			if huhu[hi] == "O":
				img1 = PhotoImage(file="icons/om.png",format='png')
				img = img1.subsample(4,4)
				label1 = Label(root,image=img)
				label1.image = img
				label1.config(background="black")
				label1.grid(row=lop,column=hi)
			elif huhu[hi] == "X":
				img1 = PhotoImage(file="icons/om1.png",format='png')
				img = img1.subsample(4,4)
				label1 = Label(root,image=img)
				label1.image = img
				label1.config(background="black")
				label1.grid(row=lop,column=hi)
			elif huhu[hi] == "U":
				img1 = PhotoImage(file="icons/om2.png",format='png')
				img = img1.subsample(4,4)
				label1 = Label(root,image=img)
				label1.image = img
				label1.config(background="black")
				label1.grid(row=lop,column=hi)
			else:
				img1 = PhotoImage(file="icons/om3.png",format='png')
				img = img1.subsample(3,3)
				label1 = Label(root,image=img)
				label1.image = img
				label1.config(background="black")
				label1.grid(row=lop,column=hi)

		lop += 1
	def winner():
		laboe = Label(root,text="WIN")
		laboe.grid(row=0,column=4)
		
	def runner():
		Main()
	root.bind("<z>",up)
	root.bind("<s>",down)
	root.bind("<d>",right)
	root.bind("<q>",left)
	root.bind("<r>",restart)	
	
men()
Main()	
mainloop()
