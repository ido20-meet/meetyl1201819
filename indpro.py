import turtle
from turtle import Turtle
from random import *
turtle.colormode(255)
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r):
		Turtle.__init__(self)
		self.penup()	
		self.shape('circle')
		self.shapesize(r/10)
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		self.goto(self.x, self.y)
	def random_color(self):
		red = randint(0,255)
		blue = randint(0,255)
		green = randint(0,255)
		self.color(red,blue,green)

	def move(self, screen_width, screen_height):
		current_x = self.xcor()
		new_x = current_x + self.dx

		current_y = self.ycor()
		new_y = current_y + self.dy
		self.random_color()
class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

q = Point(x=0, y=0)
beni = Ball(100,100,1,1,100)
beni.random_color()
beni1 = Ball(-100,-100,1,1,100)
beni1.random_color()

turtle.mainloop()