class animal(object):
	def __init__(self, name, age, gender, fav_food, make_sound):
		self.name = name
		self.age = age
		self.gender = gender
		self.fav_food = fav_food
		self.make_sound = make_sound
	def eat(self):
		print("my name is" , self.name , "and my favorite food is" , self.fav_food)
	def description(self):
		print(self.name , "is" , self.age , "years old and love eating" , self.fav_food) 
	def sound(self):
		print(self.make_sound , self.make_sound , self.make_sound)
jk = animal("fake_Mohamad", 21, "transgender", "hot choclate", "oy" )
jk.eat()
jk.description()
jk.sound()
class person(object):
	def __init__(self, name, age, gender, city, fav_color):
		self.name = name
		self.age = age
		self.gender = gender
		self.city = cuty
		self.fav_color = make_sound