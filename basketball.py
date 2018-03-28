from tkinter import*
import time
class Ball:
    def __init__(self, w, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.w = w
        self.ball = w.create_oval(self.x1, self.y1, self.x2, self.y2, fill="orange")
    def move_ball(self):
        self.w.move(self.ball,self.x1,self.y1+9.81)
        self.w.after(50,self.w.move)
g=9.81
x=5
y=5
v=h=0
game=Tk()
w = Canvas(game, width=500, height=500)

ball=Ball(w,x,y,x+10,y+10)
w.pack()
ball.move_ball()
start.mainloop()

