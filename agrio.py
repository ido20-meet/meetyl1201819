from ball1 import Ball
import time
from turtle import *
import random
import turtle
import sys
import math

turtle.tracer(0)
turtle.hideturtle()
turtle.bgcolor("green")

score = 0

RUNNING = True
sleep = 1
screen_width = turtle.getcanvas().winfo_width()/2
screen_height =turtle.getcanvas().winfo_height()/2

my_ball = Ball(0,0,10,50,25,"red")

NUMBER_OF_BALLS = 5
min_ball_r = 10
max_ball_r = 100
min_ball_dx = -5
max_ball_dx = 5
min_ball_dy = -5
max_ball_dy = 5
#min= minmum
#max= maximum
#r= radius
balls = []

for i in range (NUMBER_OF_BALLS):
	x = random.randint(int(-screen_width) + int(max_ball_r) , int(screen_width) - int(max_ball_r))
	y = random.randint(int(-screen_height) + int(max_ball_r),int(screen_height) - int(max_ball_r))
	dx = random.randint(min_ball_dx,max_ball_dx)
	if dx == 0:
		dx = random.randint(min_ball_dx,max_ball_dx)
	dy = random.randint(min_ball_dy,max_ball_dy)
	if dy == 0:
		dy = random.randint(min_ball_dy,max_ball_dy)
	radius = random.randint(min_ball_r,max_ball_r)
	color = (random.random(), random.random(), random.random())
	ball1 = Ball(x, y, dx, dy, radius, color)

	balls.append (ball1)


def move_all_balls():
	for z in balls:
		z.move(screen_width, screen_height)

def collide(ball_a, ball_b):
	ball_a_pos = ball_a.pos()
	ball_b_pos = ball_b.pos()	
	if ball_a == ball_b :
		return False
		sys.exit("Error message")
		
	ball_a.xcor()	
	ball_a.ycor()	
	ball_b.xcor()	
	ball_b.ycor()	

	DISTANCE_BETWEEN_CENTERS = ((ball_a.xcor()-ball_b.xcor())**2 + (ball_a.ycor()-ball_b.ycor())**2)**0.5

	if DISTANCE_BETWEEN_CENTERS+10 <= ball_a.radius + ball_b.radiusa:
		return True
	else:
		return False
		sys.exit("Error message")
		print("GAME OVER")

def check_all_balls_collision():
	for ball_a in balls:
		for ball_b in balls:
			if collide(ball_a,ball_b) == True:
				RADIUS_a = ball_a.r
				RADIUS_b = ball_b.r
				X_coor = random.randint(int(-screen_width) + int(max_ball_r) , int(screen_width) - int(max_ball_r))
				Y_coor = random.randint(int(-screen_height) + int(max_ball_r),int(screen_height) - int(max_ball_r))
				#coor= coordinate
				X_axis_speed = random.randint(min_ball_dx,max_ball_dx)
				while X_axis_speed == 0:
					 X_axis_speed = random.randint(min_ball_dx,max_ball_dx)
				Y_axis_speed  = random.randint(min_ball_dy,max_ball_dy)
				while Y_axis_speed  == 0:
					Y_axis_speed  = random.randint(min_ball_dy,max_ball_dy)
				RADIUS = random.randint(min_ball_r, max_ball_r)
				r = random.randint(0,255)
				g = random.randint(0,255)
				b = random.randint(0,255)
				color = (r,g,b)

				if ball_a < ball_b:
					ball_a.goto(X_coor, Y_coor) 
					ball_a.dx = X_axis_speed 
					ball_a.dy = Y_axis_speed
					ball_a.color = color
					ball_a.r += 1
					score += 1
					score_list.append(score)
					scoreboard.clear()
					scoreboard.color("black")
					scoreboard.write("score="+str(score), font=("Arial",14, "bold"))
					ball_a.shapesize(ball_a.r/10)
					ball_b.shapesize(ball_b.r/10)

				

				else:
					ball_b.goto(X_coor, Y_coor)
					ball_b.dx = X_axis_speed 
					ball_b.dy = Y_axis_speed
					ball_b.shapesize(r/10)
					ball_b.color = color
					ball_a.shapesize(ball_b.r)
					ball_b.r += 1
					
					ball_a.shapesize(ball_a.r/10)
					ball_b.shapesize(ball_b.r/10)



				
def check_myball_collision():
	for i in balls:
		if collide(i,my_ball) == True:
			r_i = i.r
			r_my_ball= my_ball.r
			ball_a = my_ball
			ball_b = i
			if my_ball.r <= i.r:
				RUNNING = False
				turtle.goto(-200,0)
				turtle.color("red")
				turtle.write("GAME OVER", move=False, font=("Arial", 50, "bold"))
				
				sys.exit("ERROR")


			else:
				X_coor = random.randint(int(-screen_width) + int(max_ball_r) , int(screen_width) - int(max_ball_r))
				Y_coor = random.randint(int(-screen_height) + int(max_ball_r),int(screen_height) - int(max_ball_r))
				X_axis_speed = random.randint(min_ball_dx,max_ball_dx)
				while X_axis_speed == 0:
					X_axis_speed = random.randint(min_ball_dx,max_ball_dx)
				Y_axis_speed  = random.randint(min_ball_dy,max_ball_dy)
				while Y_axis_speed  == 0:
					Y_axis_speed  = random.randint(min_ball_dy,max_ball_dy)
				radius = random.randint(min_ball_r, max_ball_r)
				r = random.randint(0,255)
				g = random.randint(0,255)
				b = random.randint(0,255)
				color = (r,g,b)

			
				ball_b.goto(X_coor, Y_coor)
				ball_b.dx = X_axis_speed 
				ball_b.dy = Y_axis_speed
				ball_b.shapesize(r/10)
				ball_b.color(color)
				ball_a.r = ball_a.r+1 
				ball_a.shapesize(ball_a.r/10)

			
	return True

def movearound(event):
	NEW_X_coor = event.x - screen_width
	NEW_Y_coor = -(event.y - screen_height)
	my_ball.goto(NEW_X_coor, NEW_Y_coor)
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

if score == 15:
	RUNNING = False
	turtle.color("red")
	turtle.write("you won!", move=False, font=("Arial", 50, "bold"))

while RUNNING == True:
	if screen_width!=turtle.getcanvas().winfo_width()/2 or screen_height!=turtle.getcanvas().winfo_height()/2 :
		screen_width=turtle.getcanvas().winfo_width()/2 
		screen_height=turtle.getcanvas().winfo_height()/2



	#check_all_balls_collision()
	move_all_balls()
	check_myball_collision()

	getscreen().update()
	time.sleep(sleep)
	

mainloop()