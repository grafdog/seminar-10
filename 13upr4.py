import turtle
n = int(input())
def lol(l, n):
    if n == 0:
        turtle.forward(l)
    else:
        lol(l,n-1)
        turtle.left(90)
        lol(l,n-1)
        turtle.right(90)
        lol(l,n-1)
        turtle.right(90)
        lol(l,n-1)
        lol(l,n-1)
        turtle.left(90)
        lol(l,n-1)
        turtle.left(90)
        lol(l,n-1)
        turtle.right(90)
        lol(l,n-1)
turtle.speed('slow')
lol(12,n)
