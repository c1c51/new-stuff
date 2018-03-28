from tkinter import *
costs=[22.5,5.99,7.99,60,1.1,65,16]
customers=[["bob","jill","grant","steve"],[]]
start=Tk()
variable = StringVar(start)
variable.set("one")


def begin():
    global welcome_text,view_customers
    welcome_text=Label(start,text="Hello what would you like to do")
    welcome_text.pack()
    view_customers=Button(start,text="View Customers",command=viewcustomers)
    view_customers.pack()


def viewcustomers():
    global welcome_text,view_customers
    welcome_text.pack_forget()
    view_customers.pack_forget()
    customer=OptionMenu(start, variable, customers[0])
    customer.pack()
            




begin()
