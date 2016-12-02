import turtle
turtle.speed('normal')
def levi (l,n):
    if n==0:
        turtle.forward(l)
    else:
        turtle.left(45)
        levi(l*2**(0.5)/(2),n-1)
        turtle.right(90)
        levi(l*2**(0.5)/(2),n-1)
        turtle.left(45)

levi(20,8)