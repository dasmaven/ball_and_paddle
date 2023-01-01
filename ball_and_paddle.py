
import turtle
import time




# Step 1 : Create the window in which the game will be played
window = turtle.Screen()
window.title("Let's Play !!!")
window.bgcolor("slategray")
window.setup(width = 900, height = 600)
window.tracer(0)

# Step 2 : Let's create a paddle for hitting the ball
paddle = turtle.Turtle() # Turtle() is a class that is why written with capital 'T'
paddle.speed(0)
paddle.shape("square")
paddle.color("gold")
paddle.shapesize(stretch_wid=0.3, stretch_len=7)
paddle.penup()
paddle.goto(0,-240)

# Step 3 : Let's create a ball that will hit the walls and the paddle
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("gold")
ball.penup()
ball.goto(0,0)

# delta increment in x,y coordinates for moving the ball
ball.dx = 0.2
ball.dy = 0.2

# Step 4 : Create a line that act as a trap for the ball
line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("crimson")
line.shapesize(stretch_wid=.03, stretch_len=50)
line.penup()
line.goto(0,-275)

# Step 5 : Player instructions at the bottom of the trap line
pen = turtle.Turtle()
pen.speed(0)
pen.color("mediumblue")
pen.penup()
pen.hideturtle()
pen.goto(0,-293)
pen.write("use left arrow <-- key to move left | use right arrow --> key to move right",align = "center", font = ("Courier", 11, "normal"))

# Step 8 : Function to moove the paddle with left and right arrow key
def paddle_left():
	x = paddle.xcor()
	x += -20
	if x > -390:
		paddle.setx(x)
	else:
		paddle.setx(-380)

def paddle_right():
	x = paddle.xcor()
	x += 20
	if x < 390:
		paddle.setx(x)
	else:
		paddle.setx(380)



# Step 10 : variables
ball_speed = 1
collision_counter = 1
time_played = 0.0
play_timer = True

# Step 10 : Create timer
time_elapsed = turtle.Turtle()
time_elapsed.hideturtle()
start = time.time()
game_end = turtle.Turtle()
game_end.hideturtle()

def stop_game():
	global play_timer
	play_timer = False
	
def restart_game():
	ball.goto(0,0)
	ball.color("gold")
	ball.dx = 0.2
	ball.dy = 0.2
	ball_speed = 1
	paddle.goto(0,-240)
	collision_counter = 1
	game_end.clear()

# Step 9 : key binding and listen for input
window.listen()
window.onkeypress(paddle_left,"Left")
window.onkeypress(paddle_right,"Right")
window.onkeypress(restart_game, "space")



# Main loop of the game where all the action is happening
while True:

	window.update() # update the screen with all the defined to be displayed on the screen

	# Step 6 : Let's move the ball by adding dx,dy value to the x,y coordinates
	ball.setx(round(ball.xcor(),1) + ball.dx)
	ball.sety(round(ball.ycor(),1) + ball.dy)


	# Step 7 : Create boundary collisions for the ball
	# Condition for the vertical edges aka x-axis
	if ball.xcor() >= 435:
		ball.setx(435)
		ball.dx *= -1
		collision_counter += 1
		if collision_counter % 5 == 0 and collision_counter < 20:
			ball_speed += 0.2
			ball.dx *= round(ball_speed,1)
			
	if ball.xcor() <= -440:
		ball.setx(-440)
		ball.dx *= -1
		collision_counter += 1
		if collision_counter % 5 == 0 and collision_counter < 20:
			ball_speed += 0.2
			ball.dx *= round(ball_speed,1)

	# Condition for the horizonal upper edge aka y-axis
	if ball.ycor() >= 290:
		ball.sety(290)
		ball.dy *= -1
		if collision_counter % 5 == 0 and collision_counter < 20:
			ball.dy *= round(ball_speed,1)

	# Condition for the lower edge is different because game will end here
	if ball.ycor() <= -290:
		ball.sety(-285)
		ball.color("red")
		window.update()
		ball.dy *= 0
		stop_game()

	# Create ball collision with the paddle
	if (ball.ycor() <= -230 and ball.ycor() >= -240) and (ball.xcor() <= paddle.xcor()+70 and ball.xcor() >= paddle.xcor()-70):
		ball.sety(-230)
		ball.dy *= -1
		if collision_counter % 5 == 0 and collision_counter < 20:
			ball.dy *= round(ball_speed,1)


	# Display Time Elapsed
	if play_timer == True:
		time_elapsed.hideturtle()
		time_elapsed.clear()
		time_elapsed.goto(0,260)
		time_elapsed.color("aliceblue")

		# Assign value of the time elasped to the variable before displaying the time_elapsed as sometimes it could lead to increase in decimal point by the time
		# it took execute the write command.
		time_played = round((float(time.time() - start)),1) 
		time_elapsed.write("time elpased :  {} ".format(time_played), align = "center", font = ("Courier", 13, "normal"))
			

	else:
		window.update()		
		game_end.penup()
		game_end.goto(0,50)
		game_end.color("aliceblue")
		game_end.write("Game Over : You Played for {} seconds".format(time_played), align = "center", font = ("Courier", 13, "bold"))
		game_end.goto(0,0)
		game_end.write("press spacebar to play again", align = "center", font = ("Courier", 13, "normal"))
		play_timer = True
	
		


	
		
		
	

	# Condition to increase the speed of the ball
	



# need this to keep the screen even when the main game loop while == False
window.mainloop()
