'''
import turtle
for i in range(5):
	turtle.forward(300)
	turtle.right(145)
turtle.mainloop()
''' 
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