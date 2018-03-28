from tkinter import *
start=Tk()
score=Tk()
n=s=0
name="placehold"
def one():
    global button2,text,buttona,buttond,buttone,text1,buttonb,s,text_score,text2,n,try_again,button3,name,text3
    text.pack_forget()
    text2.pack()
    button2.pack_forget()
    text1=Label(start,text=q[0][0])
    text1.pack()
    buttona=Button(start,text=q[1][0],command=correct0)
    buttona.pack()
    buttond=Button(start,text=q[1][1],command=incorrect0)
    buttond.pack()
    buttone=Button(start,text=q[1][2],command=incorrect0)
    buttone.pack()
    text1.pack()
def correct0():
    global button2,text,buttona,buttond,buttone,text1,buttonb,s,text_score,text2,n,try_again,button3,name,text3
    buttona.pack_forget()
    buttond.pack_forget()
    buttone.pack_forget()
    text1.pack_forget()
    text2.pack_forget()
    s+=1
    text=Label(start,text="correct")
    text.pack()
    buttonb=Button(start,text="Continue",command=two)
    buttonb.pack()
    text2=Label(score,text=s)
    text2.pack()
def incorrect0():
    global button2,text,buttona,buttond,buttone,text1,buttonb,s,text_score,text2,n,try_again,button3,name,text3
    buttona.pack_forget()
    buttond.pack_forget()
    buttone.pack_forget()
    text1.pack_forget()
    text=Label(start,text="incorrect")
    text.pack()
    buttonb=Button(start,text="Continue",command=two)
    buttonb.pack()
def two():
    global button2,text,buttona,buttond,buttone,text1,buttonb,s,text_score,text2,n,try_again,button3,name,text3
    n+=1
    text.pack_forget()
    buttonb.pack_forget()
    text1=Label(start,text=q[0][n])
    text1.pack()
    buttona=Button(start,text="A: The CPU completes the instruction",command=A)
    buttona.pack()
    buttond=Button(start,text="B: The CPU fetches the instruction and data needed for the instruction",command=B)
    buttond.pack()
    buttone=Button(start,text="C: The CPU understands the instruction",command=C)
    buttone.pack()
def A():
    global button2,text,buttona,buttond,buttone,text1,buttonb,s,text_score,text2,n,try_again,button3,name,text3
    buttona.pack_forget()
    buttond.pack_forget()
    buttone.pack_forget()
    text1.pack_forget()
    if n==3:
        text=Label(start,text="Correct")
        text.pack()
        buttonb=Button(start,text="Continue",command=five)
        buttonb.pack()
        text2.pack_forget()
        s+=1
        text2=Label(score,text=s)
        text2.pack()
    else:
        text=Label(start,text="incorrect")
        text.pack()
        buttonb=Button(start,text="Continue",command=two)
        buttonb.pack()
def B():
    global button2,text,buttona,buttond,buttone,text1,buttonb,s,text_score,text2,n,try_again,button3,name,text3
    buttona.pack_forget()
    buttond.pack_forget()
    buttone.pack_forget()
    text1.pack_forget()
    if n==1:
        text=Label(start,text="Correct")
        text.pack()
        text2.pack_forget()
        buttonb=Button(start,text="Continue",command=two)
        buttonb.pack()
        s+=1
        text2=Label(score,text=s)
        text2.pack()
    elif n==3:
        text=Label(start,text="incorrect")
        text.pack()
        buttonb=Button(start,text="Continue",command=five)
        buttonb.pack()
    else:
        text=Label(start,text="incorrect")
        text.pack()
        buttonb=Button(start,text="Continue",command=two)
        buttonb.pack()
def C():
    global button2,text,buttona,buttond,buttone,text1,buttonb,s,text_score,text2,n,try_again,button3,name,text3
    buttona.pack_forget()
    buttond.pack_forget()
    buttone.pack_forget()
    text1.pack_forget()
    if n==2:
        text=Label(start,text="Correct")
        text.pack()
        text2.pack_forget()
        buttonb=Button(start,text="Continue",command=two)
        buttonb.pack()
        s+=1
        text2=Label(score,text=s)
        text2.pack()
    elif n==3:
        text=Label(start,text="incorrect")
        text.pack()
        buttonb=Button(start,text="Continue",command=five)
        buttonb.pack()
    else:
        text=Label(start,text="incorrect")
        text.pack()
        buttonb=Button(start,text="Continue",command=two)
        buttonb.pack()
def five():
    global button2,text,buttona,buttond,buttone,text1,buttonb,s,text_score,text2,n,try_again,button3,name,text3
    text.pack_forget()
    buttonb.pack_forget()
    text=Label(start,text="Well done on completing the quiz. Your score is:")
    text.pack()
    text3=Label(start,text=s)
    text3.pack()
    text1=Label(start,text="Would you like to save your score?")
    text1.pack()
    button3=Button(start,text="Yes",command=namefind)
    button3.pack()
    button2=Button(start,text="No",command=fin)
    button2.pack()
def namefind():
    global button2,text,buttona,buttond,buttone,text1,buttonb,s,text_score,text2,n,try_again,button3,name,text3
    text.pack_forget()
    text3.pack_forget()
    button3.pack_forget()
    button2.pack_forget()
    text1.pack_forget()
    text=Label(start,text="Enter your name:")
    text.pack()
    text1=Entry(start,textvariable=name)
    text1.pack()
    button2=Button(start,text="Continue",command=save)
    button2.pack()
def save():
    global button2,text,buttona,buttond,buttone,text1,buttonb,s,text_score,text2,n,try_again,button3,name,text3
    name=text1.get()
    text.pack_forget()
    button2.pack_forget()
    text1.pack_forget()
    f=open("score.txt","a");
    f.write(name);
    f.write(":\n");
    s=str(s);
    f.write(s);
    f.write("\n");
    f.close()
    name=0
    text=Label(start,text="Score saved")
    text.pack()
    button2.config(command=fin)
    button2.pack()
def fin():
    global button2,text,buttona,buttond,buttone,text1,buttonb,s,text_score,text2,n,try_again,button3,name,text3
    text.pack_forget()
    text1.pack_forget()
    text3.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    text1=Label(start,text="Would you like to quit or try again?")
    text1.pack()
    button3=Button(start,text="quit",command=end)
    try_again=Button(start,text="try again",command=again)
    button3.pack()
    try_again.pack()
def end():
    global button2,text,buttona,buttond,buttone,text1,buttonb,s,text_score,text2,n,try_again,button3,name ,text3
    button3.pack_forget()
    text.pack_forget()
    text1.pack_forget()
    try_again.pack_forget()
    quit()
def again():
    global button2,text,buttona,buttond,buttone,text1,buttonb,s,text_score,text2,n,try_again,button3,name,text3
    text2.pack_forget()
    s=n=0
    text2=Label(score,text=s)
    button3.pack_forget()
    text2.pack()
    text.pack_forget()
    text1.pack_forget()
    try_again.pack_forget()
    one()
text=Label(start,text="Hello, Welcome to my Fetch, Execute cycle quiz")
text.pack()
button2=Button(start,text="continue",command=one)
button2.pack()
text_score=Label(score,text="Your score is:")
text2=Label(score,text=s)
text_score.pack()
text2.pack()
q=[["How many parts does the fetch exectute cycle have?","What happens in the fetch section?","What happens in the decode section?","What happens in the execute section?"],["A: 3","B: 4","C: 2"],["A: The CPU completes the instruction","B: The CPU fetches the instruction and data needed for the instruction","C: The CPU understands the instruction"]]








