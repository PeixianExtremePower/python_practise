import turtle as t

t.penup()
t.seth(-90)
t.fd(160)
t.pendown()
t.pensize(20)
t.colormode(255)
for j in range(20):
    t.speed(1000)
    t.pencolor(12*j,3*j,8*j)
    t.seth(130)
    if j==9:
        t.fillcolor(25*j,5*j,15*j)
        t.begin_fill()
    if j==19:
        t.fillcolor(12*j,3*j,8*j)
        t.begin_fill()
    t.fd(220)
    for i in range(23):
        t.circle(-80,10)
    t.seth(100)
    for i in range(23):
        t.circle(-80,10)
    t.fd(220)
    if j==9:
        t.end_fill()
    if j==19:
        t.end_fill()
t.done()
