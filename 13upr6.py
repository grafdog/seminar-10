import turtle
turtle.speed('fastest')
def drak (l,n,an = 45):
    if n==0:
        turtle.forward(l)
    else:
        turtle.right(an)
        drak(l/2,n-1,45)
        turtle.left(an * 2)
        drak(l/2,n-1,-45)
        turtle.right(an)

drak(100000,14)
turtle.done()