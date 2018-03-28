#Adam Rook 8U 06/10/15
def solve():
    global a,b,hyp
    hyp=((a*a)+(b*b)) ** (0.5) 
while True:
    print("hello and welcome to a hypothernes solver")
    print("what is one side")
    a=int(input())
    print("the other?")
    b=int(input())
    solve()
    print("your hypothernes is " ,hyp)
