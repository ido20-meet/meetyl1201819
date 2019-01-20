import turtle 

class Ball(Turtle):
	def __inint__(self,x,y,dx,dy,r,color):
		Turtle.__inint__(self)
		self.x=x
		self.y=y
		self.dx=dx
		self.dy=dy