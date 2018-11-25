from turtle import *
import turtle
import random

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)


ball1 = Ball(20, "blue", 5)
ball2 = Ball(15, "red", 5)

def check_collision(ball1, ball2):
	D = math.sqrt(math.pow((ball2.xcor()-ball1.xcor()),2) + math.pow((yball2.ycor()-ball1.ycor()),2))
	if D <= ball1.radius + ball2.radius:
		print("the balls are collide!")
	if D > ball1.radius + ball2.radius:
		print("the balls are NOT collide!")
check_collision(ball1,ball2)

turtle.mainloop()
