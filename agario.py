import turtle
from turtle import Turtle
from random import *
turtle.setup(1000,900)
turtle.tracer(0, 0)

turtle.colormode(255)
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r):
		Turtle.__init__(self)
		self.penup()	
		self.shape('circle')
		self.shapesize(r/10)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.goto(x, y)
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
MY_BALL = Ball(1,1,100)
MY_BALL.random_color()
beni1 = Ball(1,1,100)
beni1.random_color()

turtle.update()

screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

while True:
	MY_BALL.move(screen_width,screen_height)
	
