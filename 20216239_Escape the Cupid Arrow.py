# Name: Hu, Yao Chieh
# Student ID: 20216239
# Email Address: jj1385jeff850527@gmail.com
# There will be one second wait after clicking start!
# So, don't be too excited or nervous!
# The heart will automatically move to the place you ready to start!

# COMP1021 Jeff's Game_Escape the Cupid's arrows


import turtle
import random
import time
import pygame



#initialization and oringinal setting

pygame.init()
pygame.mixer.init(buffer=16)

heartbeat=pygame.mixer.Sound('Heart.wav')
cupid=pygame.mixer.Sound('Cupid.wav')
scream=pygame.mixer.Sound('Scream.wav')
cp=1
hp=0
finalarrow=100

window_height = 600
window_width = 600

update_interval = 40

river_width = 300
minimum_river_width = 100
border_height = 600
river_width_update = 0.5
safe_distance_from_border = border_height / 2 + 3

score=0
first=0

croc_number = 17
crocs = []
croc_speeds = []
croc_width = 100
croc_height = 40
croc_speed_min, croc_speed_max = 4, 17

safe_distance_from_croc = 20


#Define Functions!!!!

def gameover():    
    global score
    global hp
    global finalarrow
    
    pygame.mixer.stop()
    scream.play()
    print("Heartbroken! Your Score is "+str(score))
    #turtle.write(msg+"! Your Score is "+str(score), align="center", font=("Arial", 24, "normal"))
    hp=0

    topic_turtle.clear()
    topic_turtle.goto(0,100)
    topic_turtle.pencolor("black")
    topic_turtle.write("Oh no! Your heart is broken!", font=("Arial", 22, "bold"), align="center")

    score_text.clear()
    score_text.goto(0,50)
    score_text.pencolor("red")
    score_text.write("Your final score: "+str(score) , font=("Arial", 32, "bold"), align="center")

    turtle.done()
    
    
def moveplayerturtle(x, y):

    if x > -window_width / 2 and x < window_width / 2:
        turtle.goto(x, y)
'''
def moveplayerturtles(x, y):

    if x > -window_width / 2 and x < window_width / 2:
        turtle.goto(x, y)
'''

def decrease_speed(x, y):
    global croc_speed_max
    global croc_speed_min
    if croc_speed_max > croc_speed_min :
        croc_speed_max-=1
        speed_turtle.clear()
        speed_turtle.write(str(croc_speed_max), align="center")

def increase_speed(x, y):
    global croc_speed_max
    global croc_speed_min
    if croc_speed_max < 41 :
        croc_speed_max+=1
        speed_turtle.clear()
        speed_turtle.write(str(croc_speed_max), align="center")

def decrease_number(x,y):
    global croc_number
    if croc_number > 4 :
        croc_number-=1
        number_turtle.clear()
        number_turtle.write(str(croc_number), align="center")
        crocs.pop()

def increase_number(x,y):
    global croc_number
    if croc_number < 41 :
        croc_number+=1
        number_turtle.clear()
        number_turtle.write(str(croc_number), align="center")

        croc = turtle.Turtle()
        croc.shape("lovearrow.gif")
        croc.left(180)
        croc.up()
        x = (window_width + croc_width) / 2
        y = random.uniform(-(river_width-croc_height)/2, (river_width-croc_height)/2)
        croc.goto(x, y)
        
        crocs.append(croc)

def Heartplay():
    global hp
    
    if hp ==1:    
        heartbeat.play()
        turtle.ontimer(Heartplay,1000)        


def updatescreen():

    global river_width
    global score
    global river_width_update
    global finalarrow
    global first

    if first ==1:
        topic_turtle.pencolor("white")
        topic_turtle.up()
        topic_turtle.goto(0, 170)
        topic_turtle.write("Ready?", font=("Arial", 30, "bold"),align="center")
        time.sleep(1)
        topic_turtle.undo()
        topic_turtle.write("GO!!!", font=("Arial", 30, "bold"),align="center")
        first=0
        
    
    
    if river_width >= minimum_river_width:
    
        upper_river_border.sety(upper_river_border.ycor() - river_width_update)
        lower_river_border.sety(lower_river_border.ycor() + river_width_update)

        river_width-=(2*river_width_update)

    
    if upper_river_border.ycor() - turtle.ycor() < safe_distance_from_border:
        gameover()
        return

    if turtle.ycor()-lower_river_border.ycor() < safe_distance_from_border:
        gameover()
        return




    
    for i in range(croc_number):        
        
        if crocs[i].xcor() < -(window_width+croc_width)/2:
            x = (window_width+croc_width)/2
            y = random.uniform(lower_river_border.ycor() + safe_distance_from_border,upper_river_border.ycor() - safe_distance_from_border) #y position within the two river borders
            crocs[i].goto(x, y)
            croc_speeds[i] = random.uniform(croc_speed_min, croc_speed_max)# speed valuecrocs[i].forward(croc_speeds[i])
            score+=100
            score_text.clear()
            score_text.write(score, font=("Arial", 20, "bold"), align="center")
        
        crocs[i].forward(croc_speeds[i])
        

        if turtle.distance(crocs[i]) < safe_distance_from_croc:

            gameover()
            return

    turtle.update()
    turtle.ontimer(updatescreen, update_interval)


def startgame(x,y):

    global cp
    global hp
    global score
    global first
    
    turtle.onscreenclick(moveplayerturtle)    
    turtle.ondrag(moveplayerturtle)

    left_turtle.hideturtle()
    right_turtle.hideturtle()
    left2_turtle.hideturtle()
    right2_turtle.hideturtle()
    left_turtle.goto(300,300)
    right_turtle.goto(300,300)
    left2_turtle.goto(300,300)
    right2_turtle.goto(300,300)
    start_button.goto(300,300)
    


    pygame.mixer.stop()
    cp=0
    hp=1
    Heartplay()   
 

    label_turtle.clear()
    label2_turtle.clear()
    start_button.clear()
    speed_turtle.clear()
    number_turtle.clear()
    topic_turtle.clear()

    score_text.pencolor("red")
    score_text.write(score, font=("Arial", 20, "bold"), align="center")
    topic_turtle.goto(0,250)
    topic_turtle.pencolor("white")
    topic_turtle.write("SCORE:", font=("Arial", 20, "bold"), align="center")

    
    for _ in range(croc_number):    
        croc_speeds.append(random.uniform(croc_speed_min, croc_speed_max))


    turtle.update()
    
    
    


    #time.sleep(1)
    first=1
    updatescreen()
    
    #turtle.ontimer(updatescreen,1000)

    #turtle.ontimer(updatescreen,update_interval)    


def Cupidplay():
    global cp
    
    if cp ==1:    
        cupid.play()        
        turtle.ontimer(Cupidplay,30000)




#Entry!!!!!!!!!!!!!!!!!!!


# Part 1
turtle.setup(window_width, window_height) # Set the window size
turtle.bgcolor("lightgray")

# Part 3 (1 of 4)
# 3.1. Turn off the tracer here
turtle.tracer(False)

turtle.addshape("lovearrow.gif")
#croc_number = 20
#print(croc_number)
for _ in range(croc_number):

    croc = turtle.Turtle()
    croc.shape("lovearrow.gif")
    croc.left(180)
    croc.up()
    x = (window_width + croc_width) / 2
    y = random.uniform(-(river_width-croc_height)/2, (river_width-croc_height)/2)
    croc.goto(x, y)
    
    crocs.append(croc)

    #print(croc_number)

# Part 4.1
# 4.1.1. Create the big boxes for upper border and lower border
upper_river_border = turtle.Turtle()
upper_river_border.up()
lower_river_border = turtle.Turtle()
lower_river_border.up()

turtle.addshape("upper_river_border.gif")
upper_river_border.shape("upper_river_border.gif")
turtle.addshape("lower_river_border.gif")
lower_river_border.shape("lower_river_border.gif")



# 4.1.5. Set the initial y position of the borders
upper_river_border.sety((border_height + river_width) / 2)
lower_river_border.sety(-(border_height + river_width) / 2)







# Prepare the player turtle
turtle.addshape("heart2.gif")
turtle.shape("heart2.gif")
#turtle.color("GreenYellow")
turtle.up()

label_turtle=turtle.Turtle()
label_turtle.hideturtle()
label_turtle.pencolor("red")
label_turtle.up()
label_turtle.goto(-120, 100) # Put the text next to the spinner control
label_turtle.write("Maximum Speed of Arrows:", font=("Arial", 8, "bold"))

speed_turtle=turtle.Turtle()
speed_turtle.hideturtle()
speed_turtle.pencolor("red")
speed_turtle.up()
speed_turtle.goto(100, 100) # Put the text next to the spinner control
speed_turtle.write(str(croc_speed_max), align="center")

left_turtle=turtle.Turtle()
left_turtle.shape("arrow")
left_turtle.color("red")
left_turtle.shapesize(0.5,1)
left_turtle.left(180)
left_turtle.up()
left_turtle.goto(80, 108) # Put the text next to the spinner control

right_turtle=turtle.Turtle()
right_turtle.shape("arrow")
right_turtle.color("red")
right_turtle.shapesize(0.5,1)
right_turtle.up()
right_turtle.goto(120, 108)





label2_turtle=turtle.Turtle()
label2_turtle.hideturtle()
label2_turtle.pencolor("red")
label2_turtle.up()
label2_turtle.goto(-120, 80) # Put the text next to the spinner control
label2_turtle.write("Maximum Number of Arrows:", font=("Arial", 8, "bold"))

number_turtle=turtle.Turtle()
number_turtle.hideturtle()
number_turtle.pencolor("red")
number_turtle.up()
number_turtle.goto(100, 80) # Put the text next to the spinner control
number_turtle.write(str(croc_speed_max), align="center")

left2_turtle=turtle.Turtle()
left2_turtle.shape("arrow")
left2_turtle.color("red")
left2_turtle.shapesize(0.5,1)
left2_turtle.left(180)
left2_turtle.up()
left2_turtle.goto(80, 88) # Put the text next to the spinner control

right2_turtle=turtle.Turtle()
right2_turtle.shape("arrow")
right2_turtle.color("red")
right2_turtle.shapesize(0.5,1)
right2_turtle.up()
right2_turtle.goto(120, 88)



topic_turtle=turtle.Turtle()
topic_turtle.hideturtle()
topic_turtle.pencolor("white")
topic_turtle.up()
topic_turtle.goto(-184, 250)
topic_turtle.write("Escape the Cupid's Arrows!!", font=("Arial", 20, "bold"))
topic_turtle.pencolor("yellow")
topic_turtle.goto(-180, 230)
topic_turtle.write("Please choose the number and speed of arrows", font=("Arial", 12, "bold"))
topic_turtle.goto(-180, 210)
topic_turtle.write("To have a crush, please press the 'LOVE' button", font=("Arial", 12, "bold"))
topic_turtle.goto(-270, 190)
topic_turtle.write("You need to drag the heart using the mouse to escape those bad arrows", font=("Arial", 12, "bold"))
topic_turtle.goto(-260, 170)
topic_turtle.write("The heart will break when you shot by an arrow or touch the boundary", font=("Arial", 12, "bold"))



start_button = turtle.Turtle()
start_button.up()
start_button.goto(-40, 45)
start_button.color("red")
start_button.begin_fill()
for _ in range(2):
    start_button.forward(80)
    start_button.left(90)
    start_button.forward(25)
    start_button.left(90)
    
start_button.end_fill()
start_button.color("white")
start_button.goto(0, 50)
start_button.write("LOVE", font=("Arial", 10, "bold"), align="center")

start_button.goto(0, 58)
start_button.shape("square")
start_button.shapesize(1.25, 4)
start_button.color("")


score_text=turtle.Turtle()
score_text.up()
score_text.hideturtle()
score_text.goto(0, 220)


    
Cupidplay()


left_turtle.onclick(decrease_speed)
right_turtle.onclick(increase_speed)
left2_turtle.onclick(decrease_number)
right2_turtle.onclick(increase_number)

start_button.onclick(startgame)



turtle.update()
#turtle.listen()

turtle.done()

 
