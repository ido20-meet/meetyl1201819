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
	def __init__(self, name, age, gender, city, fav_color, fav_game):
		self.name = name
		self.age = age
		self.gender = gender
		self.city = city
		self.fav_color = fav_color
		self.fav_game = fav_game
	def living(self):
		print("my name is", self.name, "and i live at", self.city)
	def gaming(self):
		print("btw my favorite game is", self.fav_game, "let's go play", self.fav_game)
ido = person("ido", 16, "male", "tzour hadassa", "blue", "fortnite")
ido.living()
ido.gaming()
