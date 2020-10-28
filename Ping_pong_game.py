import turtle
win=turtle.Screen()
win.title("my first game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#Padle1
pad1=turtle.Turtle()
pad1.speed(0)
pad1.shape("square")
pad1.color("pink")
pad1.shapesize(stretch_wid=5,stretch_len=1)#size of sqare
pad1.penup()
pad1.goto(-350, 0)


#padle2
pad2=turtle.Turtle()
pad2.speed(0)
pad2.shape("square")
pad2.color("yellow")
pad2.shapesize(stretch_wid=5,stretch_len=1)#size of sqare
pad2.penup()
pad2.goto(+350, 0)

#scoring
scor1=0
scor2=0


#ball
bal=turtle.Turtle()
bal.speed(0)
bal.shape("circle")
bal.color("white")
bal.penup()
bal.goto(0, 0)
bal.chx=0.3
bal.chy=0.3

#message
pen=turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1:0 Player2:0",align="center", font=("Courier",24,"normal"))

#Function to move
def pad1_up():
    y =pad1.ycor()
    y+=20
    pad1.sety(y)#changing cordin
def pad1_down():
    y =pad1.ycor()
    y-=20
    pad1.sety(y)#changing cordin
def pad2_up():
    y =pad2.ycor()
    y+=20
    pad2.sety(y)#changing cordin
def pad2_down():
    y =pad2.ycor()
    y-=20
    pad2.sety(y)#changing cordin

#Keyboard click
win.listen()
win.onkeypress(pad1_up,"w")
win.onkeypress(pad1_down,"s")
win.onkeypress(pad2_up,"8")
win.onkeypress(pad2_down,"2")
#main loop
while True:
    win.update()
    

    #ball movement
    bal.setx(bal.xcor()+bal.chx)
    bal.sety(bal.ycor()+bal.chy)

    #border for pad
    if pad1.ycor()>250:
        pad1.sety(250)
    if pad2.ycor()>250:
        pad2.sety(250)
    if pad1.ycor()<-250:
        pad1.sety(-250)
    if pad2.ycor()<-250:
        pad2.sety(-250)
        
    #border
    if bal.ycor()>290:
        bal.sety(290)
        bal.chy*=-1
    if bal.ycor()<-290:
        bal.sety(-290)
        bal.chy*=-1
    if bal.xcor()>390:
        bal.goto(0,0)
        bal.chx*=-1
        scor1+=1
        pen.clear()
        pen.write("Player 1:{} Player2:{}".format(scor1,scor2),align="center", font=("Courier",24,"normal"))
    if bal.xcor()<-390:
        bal.goto(0,0)
        bal.chx*=-1
        scor2+=1
        pen.clear()
        pen.write("Player 1:{} Player2:{}".format(scor1,scor2),align="center", font=("Courier",24,"normal"))
    #collision
    if (bal.xcor() > 340 and bal.xcor()<350 and (bal.ycor() < pad2.ycor()+50 and bal.ycor() > pad2.ycor()-50)):
        bal.setx(340)
        bal.chx*=-1

    if (bal.xcor() < -340 and bal.xcor()>-350 and (bal.ycor() < pad1.ycor()+50 and bal.ycor() > pad1.ycor()-50)):
        bal.setx(-340)
        bal.chx*=-1