from tkinter import *
import random
s=Tk()
def one():
    global x,b1,b2,b3,b4,b5,b6,b7,b8,b9,z
    z=1
    b1=Button(s,text="X",command=one).grid(row=0, column=0)
    pc()
def two():
    global x,b1,b2,b3,b4,b5,b6,b7,b8,b9,z
    z=2
    b2=Button(s,text="X",command=two).grid(row=0, column=1)
    pc()
def three():
    global x,b1,b2,b3,b4,b5,b6,b7,b8,b9,z
    z=3
    b3=Button(s,text="X",command=three).grid(row=0, column=2)
    pc()
def four():
    global x,b1,b2,b3,b4,b5,b6,b7,b8,b9,z
    z=4
    b4=Button(s,text="X",command=four).grid(row=1, column=0)
    pc()
def five():
    global x,b1,b2,b3,b4,b5,b6,b7,b8,b9,z
    z=5
    b5=Button(s,text="X",command=five).grid(row=1, column=1)
    pc()
def six():
    global x,b1,b2,b3,b4,b5,b6,b7,b8,b9,z
    z=6
    b6=Button(s,text="X",command=six).grid(row=1, column=2)
    pc()
def seven():
    global x,b1,b2,b3,b4,b5,b6,b7,b8,b9,z
    z=7
    b7=Button(s,text="X",command=seven).grid(row=2, column=0)
    pc()
def eight():
    global x,b1,b2,b3,b4,b5,b6,b7,b8,b9,z
    z=8
    b8=Button(s,text="X",command=eight).grid(row=2, column=1)
    pc()
def nine():
    global x,b1,b2,b3,b4,b5,b6,b7,b8,b9,z
    z=9
    b9=Button(s,text="X",command=nine).grid(row=2, column=2)
    pc()
def pc():
    global x,b1,b2,b3,b4,b5,b6,b7,b8,b9,z
    x=random.randint(1,9)
    while x!=z:
        if x==1:
          b1=Button(s,text="O",command=one).grid(row=0, column=0)
        if x==2:
            b2=Button(s,text="O",command=two).grid(row=0, column=1)
        if x==3:
            b3=Button(s,text="O",command=three).grid(row=0, column=2)
        if x==4:
          b4=Button(s,text="O",command=four).grid(row=1, column=0)
        if x==5:
            b5=Button(s,text="O",command=five).grid(row=1, column=1)
        if x==6:
            b6=Button(s,text="O",command=six).grid(row=1, column=2)
        if x==7:
            b7=Button(s,text="O",command=seven).grid(row=2, column=0)
        if x==8:
            b8=Button(s,text="O",command=eight).grid(row=2, column=1)
        if x==9:
            b9=Button(s,text="O",command=nine).grid(row=2, column=2)
    
b1=Button(s,text="_",command=one).grid(row=0, column=0)
b2=Button(s,text="_",command=two).grid(row=0, column=1)
b3=Button(s,text="_",command=three).grid(row=0, column=2)
b4=Button(s,text="_",command=four).grid(row=1, column=0)
b5=Button(s,text="_",command=five).grid(row=1, column=1)
b6=Button(s,text="_",command=six).grid(row=1, column=2)
b7=Button(s,text="_",command=seven).grid(row=2, column=0)
b8=Button(s,text="_",command=eight).grid(row=2, column=1)
b9=Button(s,text="_",command=nine).grid(row=2, column=2)
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()
b8.pack()
b9.pack()

