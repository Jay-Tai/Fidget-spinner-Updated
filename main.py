from turtle import *
state={"turn":0}

def spinner():
    clear()
    pensize(19)
    angle=state["turn"]/10
    right(angle)
    forward(100)
    dot(100,"blue")
    penup()
    back(100)
    pendown()
    left(120)
    forward(100)
    dot(100,"yellow")
    penup()
    back(100)
    pendown()
    left(120)
    forward(100)
    dot(100,"red")
    penup()
    back(100)
    pendown()
    update()

def animate():
    if state["turn"]>0:
        state["turn"]-=1
    spinner()
    ontimer(animate,20)
def flick():
    state["turn"]+=10
setup(420,420,370,0)
hideturtle()
tracer(False)
width(20)
onkey(flick,"space")
listen()
animate()
done()