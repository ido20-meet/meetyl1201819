'''
import turtle
for i in range(5):
	turtle.forward(300)
	turtle.right(145)
turtle.mainloop()
'
import turtle
turtle.penup()
turtle.goto(100,100)
turtle.begin_fill()
turtle.pendown()
turtle.goto(100,0)
turtle.goto(0,-100)
turtle.goto(-100,0)
turtle.goto(-100,100)
turtle.goto(100,100)
turtle.end_fill()
turtle.mainloop()
'''
import turtle
turtle.register_shape("bamba.gif")
turtle.shape("bamba.gif")
asd = 1
turtle.speed(100000)
for i in range(720):
	asd = asd + 0.5
	turtle.pendown()
	turtle.right(asd)
	turtle.forward(300)
	turtle.right(45)
	turtle.forward(150)
	turtle.right(90)
	turtle.forward(50)
	turtle.penup()
	turtle.home()
turtle.mainloop()