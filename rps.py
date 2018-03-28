import random
c=0
def play():
    global a,b,c,d
    b=random.choice(['rock','paper','scissors'])
    print("your choice")
    a=str(input())
    if a==b:
        print("draw")
    if a=='rock' and b=='paper' or a=='paper' and b=='scissors' or a=='scissors' and b=='rock':
        print("lose")
        c=c-1
    if a=='rock' and b=='scissors' or a=='paper' and b=='rock' or a=='scissors' and b=='paper':
        print("win")
        c=c+1
for x in range(0, 3):
    play()
print("you scored", c)
if c>=1:
    d='win'
elif c==0:
    d='draw'
if c<0:
    d='lose'
    print("therefore you", d)


