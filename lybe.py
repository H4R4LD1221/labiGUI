#!/usr/bin/python3
import sys
import os
import time
from tkinter import messagebox


class Some:
        def __init__(self,x,o):
                self.x = x
                self.o = o
                self.lab = []
                fo = open("map.txt",'r')
                for fi in fo.readlines():
                        self.lab.append(fi)        
        def up(self):
                sys.stdout = open("map.txt",'w')
                for a in range(len(self.lab)):
                        if a == len(self.lab) - 1:
                                for w in self.lab[a]:
                                        print(w,end = "")                            
                        else:
                                for k in range(len(self.lab[a])):
                                        if (self.lab[a+1][k] == self.x) & (self.lab[a][k] != self.o):
                                                print(self.x,end="")
                                        elif self.lab[a][k] == self.x:
                                                print(" ",end="")        
                                        else:
                                                print(self.lab[a][k],end="")
        def down(self):
                sys.stdout = open("map.txt",'w')
                for a in range(len(self.lab)):
                        if a == len(self.lab) - 1:
                                for w in self.lab[a]:
                                        print(w,end = "")                            
                        else:
                                for k in range(len(self.lab[a])):
                                        if (self.lab[a-1][k] == self.x) & (self.lab[a][k] != self.o):
                                                print(self.x,end="")
                                                a -= 2
                                        elif self.lab[a][k] == self.x:
                                                print(" ",end="")
                                                a += 2        
                                        else:
                                                print(self.lab[a][k],end="")
        def left(self):
                sys.stdout = open("map.txt",'w')
                for a in range(len(self.lab)):
                        if a == len(self.lab) - 1:
                                for w in self.lab[a]:
                                        print(w,end = "")                            
                        else:
                                for k in range(len(self.lab[a])):
                                        if k == len(self.lab[a]) - 1:
                                                print(self.lab[a][k],end="")
                                        else:        
                                                if (self.lab[a][k+1] == self.x) & (self.lab[a][k] != self.o):
                                                        print(self.x,end="")
                                                elif self.lab[a][k] == self.x:
                                                        print(" ",end="")        
                                                else:
                                                        print(self.lab[a][k],end="")
        def right(self):
                back = sys.stdout
                sys.stdout = open("map.txt",'w')
                for a in range(len(self.lab)):
                        if a == len(self.lab) - 1:
                                for w in self.lab[a]:
                                        print(w,end = "")                            
                        else:
                                for k in range(len(self.lab[a])):
                                        if k == len(self.lab[a]) - 1:
                                                print(self.lab[a][k],end="")
                                        else:        
                                                if (self.lab[a][k-1] == self.x) & (self.lab[a][k] == "U"):
                                                        sys.stdout = back
                                                        os.system('clear')
                                                        with open("map_or.txt","r") as mr:
                                                                with open("map.txt",'w') as m:
                                                                        for e in mr:
                                                                                m.write(e)
                                                        messagebox.showinfo('',"YOU WIN")       
                                                        time.sleep(2)
                                                        exit(0)        
                                                elif (self.lab[a][k-1] == self.x) & (self.lab[a][k] != self.o):
                                                        print(self.x,end="")
                                                        k -= 2
                                                elif self.lab[a][k] == self.x:
                                                        print(" ",end="")
                                                        k += 2        
                                                else:
                                                        print(self.lab[a][k],end="")