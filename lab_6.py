from turtle import Turtle
import turtle
import 
class Square(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")
	def random_color(self):
		self.color()

square = Square(25)

turtle.mainloop()