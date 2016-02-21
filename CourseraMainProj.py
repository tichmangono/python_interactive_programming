
#-----------------------------------------
# EXTENDED GUESS THE NUMBER MINI-PROJ
#-----------------------------------------
# This is the same project as week 2 and allows user to input guesses
# in a range of their choice (>10) until they run out of guesses, quit,
# guess the right number
# Extra Features added
#--includes a customizable range (enter your own max number),
#	and changes the message
#--draws dynamic output msgs on canvas instead of just in console
#--Shows the results of the the last game played
#--Shows an extensive STATS or score board with
    #--games won
    #--games lost
    #--games quit i.e. you start playing a game and then decide to
    #	change the range, test this by selecting a range, guessing 
    #	less than the max number of chances, then change range
    # 	the number of games quit will increase by one
    #	and change 
    #--total played
import simplegui
import random
import math

# helper function to start and restart the game
won=lost=quit=played=0
stats="STATS: Total Played-"+str(won+lost+quit)+" | Won-"+str(won)+" | Lost-"+str(lost)+" | Quit-"+str(0)
line3= "Game "+ str(won+lost+quit+1) +" Results: In progress..."
guess_range=100
announcement="Caution: Check the console to confirm results!"

def new_game():
    # initialize global variables used in your code here
    global guess_range,chances_left,secret_number, played, line1, line2, line3
    
    line1=line2=""
    if guess_range==1000:
        secret_number=random.randrange(0,guess_range)
        chances_left=int(math.ceil(math.log(guess_range,2)))
        line1="Welcome! Guess range is: "+str(guess_range)
        line2="You have "+str(chances_left)+" chances left."
        print "\n=====\n", line1, "\n", line2
    else:
        secret_number=random.randrange(0,guess_range)
        chances_left=int(math.ceil(math.log(guess_range,2)))
        line1="Welcome! Guess range is: "+str(guess_range)
        line2="You have "+str(chances_left)+" chances left."
        print "\n=====\n", line1, "\n", line2

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global guess_range, stats, won,lost,quit,played
    
    guess_range=100
    if chances_left not in (0, int(math.ceil(math.log(guess_range,2)))):  
        quit += 1
        stats="STATS: Total Played-"+str(won+lost+quit)+" | Won-"+str(won)+" | Lost-"+str(lost)+" | Quit-"+str(quit)
    else:
        stats="STATS: Total Played-"+str(won+lost+quit)+" | Won-"+str(won)+" | Lost-"+str(lost)+" | Quit-"+str(quit)   
    new_game()
    # remove this when you add your code    
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game 
    global guess_range, stats, won,lost,quit,played
    
    guess_range=1000
    if chances_left not in (0, int(math.ceil(math.log(guess_range,2)))):
        quit += 1
        stats="STATS: Total Played-"+str(won+lost+quit)+" | Won-"+str(won)+" | Lost-"+str(lost)+" | Quit-"+str(quit)
    else:
        stats="STATS: Total Played-"+str(won+lost+quit)+" | Won-"+str(won)+" | Lost-"+str(lost)+" | Quit-"+str(quit)   
    new_game()

def input_newRange(newRange):
    # input box that lets the user choose their own range
    global line1,line2, line3
    global guess_range, stats, won,lost,quit,played
    
    if newRange.isdigit() and int(newRange)>=10:
        if chances_left not in (0, int(math.ceil(math.log(guess_range,2)))):
            guess_range=int(newRange)
            quit += 1
            stats="STATS: Total Played-"+str(won+lost+quit)+" | Won-"+str(won)+" | Lost-"+str(lost)+" | Quit-"+str(quit)
        else:
            guess_range=int(newRange)
            stats="STATS: Total Played-"+str(won+lost+quit)+" | Won-"+str(won)+" | Lost-"+str(lost)+" | Quit-"+str(quit)   
        new_game()
    elif newRange.isdigit() and int(newRange)<10:
        line1=  ":-("
        line2 = "Invalid range, range must be >10. Try again"
        print line2
    else:
        line1=  ":-("
        line2 = "Invalid range, numbers only. Try again"
        print line2
                                        
def input_guess(guess):
    # main game logic goes here	
    global line1, line2,line3,secret_number,chances_left
    global played,quit,won,lost,stats
    
    n=int(guess)
    line1="Your guess was " +str(n)
    print "\nYour Guess was",n, "."
    chances_left -=1
    
    if n==secret_number:
        won += 1
        played += 1
        #quit=played-won-lost
        line3= "Previous game results: Correct. Thank you for playing!"
        print line3
        stats="STATS: Total Played-"+str(won+lost+quit)+" | Won-"+str(won)+" | Lost-"+str(lost)+" | Quit-"+str(quit)       
        new_game()
    elif n<secret_number and chances_left>0:
        line2="Go higher. You have "+str(chances_left)+" chances left."
        print line2
    elif n>secret_number and chances_left>0:
        line2="Go lower. You have "+ str(chances_left)+" chances left."
        print line2
    else:
        lost += 1
        played += 1
        #quit=played-won-lost
        line3= "Previous game results: Game-over, the secret number was "+str(secret_number)+"." 
        print line3
        stats="STATS: Total Played-"+str(won+lost+quit)+" | Won-"+str(won)+" | Lost-"+str(lost)+" | Quit-"+str(quit)
        new_game()

def draw(canvas):
    # enables an extra draw feature to show results on canvas
    canvas.draw_text(stats, [20,150],18,"orange")
    canvas.draw_text(line3, [20,120],14,"gray")
    canvas.draw_text(line1, [20,40],20,"yellow")
    canvas.draw_text(line2, [20,70],18,"red")
    canvas.draw_text(announcement, [20,220],12,"white")

# create frame
frame=simplegui.create_frame("Guess the Number", 430,250)
input1=frame.add_input("Enter your guess below:", input_guess, 95)
input2=frame.add_input("Customize range:", input_newRange, 95)
button1=frame.add_button("Range 0-100", range100, 100)
button2=frame.add_button("Range 0-1000", range1000, 100)
frame.set_draw_handler(draw)

# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric


###########################################################
# MY SIMPLE GUI CAR, ORIGINAL PROJECT, YAY!
###########################################################
# This program will make the car move across and up the screen
# forward, right to left
# then reverse, left to right
# maybe also down and up

import simplegui

#initialize global variables for the positions
interval=1
width=1000
height=350
cruise=0.05
level=0.1
speed=cruise
altitude=0

# position the road, r
r1=[10,200] ; r2=[width-10,200]   
# position the main body of the car, b
b1=[715,185];b2=[735,185];b3=[735,155];b4=[700,155];b5=[675,135]
b6=[615,135];b7=[575,155];b8=[535,160];b9=[535,185]
# position the front door window, fd
fd1=[580,155];fd2=[615,137];fd3=[642,137];fd4=[642,155]
# position the back door window, bd
bd1=[645,155];bd2=[645,137];bd3=[675,137];bd4=[695,155]
# position the front wheel, fw
fw=[580,185]
# position the back wheel, bw
bw=[700, 185]
# position the head in the car, h
h=[625,145]
car_position=[b1,b2,b3,b4,b5,b6,b7,b8,b9,fd1,fd2,fd3,fd4,bd1,bd2,bd3,bd4,fw,bw,h]
line1="Position b1 = "+str(b1) + "and b9 = "+str(b9)

def park():
    # function to reset everything and get the car back to start
    global r1,r2, b1,b2,b3,b4,b5,b6,b7,b8,b9,fd1,fd2,fd3,fd4
    global bd1,bd2,bd3,bd4,fw,bw,h, car_position, speed, altitude
    # position the road, r
    r1=[10,200] ; r2=[width-10,200]   
    # position the main body of the car, b
    b1=[715,185];b2=[735,185];b3=[735,155];b4=[700,155];b5=[675,135]
    b6=[615,135];b7=[575,155];b8=[535,160];b9=[535,185]
    # position the front door window, fd
    fd1=[580,155];fd2=[615,137];fd3=[642,137];fd4=[642,155]
    # position the back door window, bd
    bd1=[645,155];bd2=[645,137];bd3=[675,137];bd4=[695,155]
    # position the front wheel, fw
    fw=[580,185]
    # position the back wheel, bw
    bw=[700, 185]
    # position the head in the car, h
    h=[625,145]
    car_position=[b1,b2,b3,b4,b5,b6,b7,b8,b9,fd1,fd2,fd3,fd4,bd1,bd2,bd3,bd4,fw,bw,h]
    speed=0
    altitude=0
    
# Handler for the timer
def tick_drive():
    #change position of the car to make it move forward
    global car_position, speed, altitude, position, line1,b1,b9

    for i in car_position:
        if i[0] < 0:
            i[0]= i[0] % width 
            i[0] -= speed
            #i[1] -= altitude
        elif i[0] > width:
            i[0]= i[0] % width
            i[0] -= speed
            #i[1] -= altitude
        elif i[1] < 0:
            i[1] = i[1] % height
            #i[0] -= speed
            i[1] -= altitude
        elif i[1] > height:
            i[0]= i[0] % height
            i[0] -= speed
            #i[1] -= altitude
        else: 
            i[0] -= speed
            i[1] -= altitude
    line1="Position b1 = "+str(b1) + "and b9 = "+str(b9)
# Button to go forward
def forward():
    global speed
    if speed==0:
        speed = cruise
    else:
        speed=abs(speed)
    
# Button to increase speed 
def accelerator():
    global speed
    if speed==0:
        speed = cruise
    else:
        speed *= 2

# Button to reduce speed
#def decelerator():
#    global speed
#    if speed > 0:
#        speed -= 1

# Emergency brakes
def emergency_brake():
    global speed, altitude
    speed=0
    altitude=0
    
# Button to reverse
def reverse():
    global speed
    if speed==0:
        speed = -cruise
    elif speed>0:
        speed *= -1
    else:
        pass
    
# Button to ramp up or fly
def fly():
    global b1, b9, altitude
    
    #if 20<b1[1]<186 and 20<b9[1]<186 and 20<b1[0]<980 and 20<b9[0]<980:
    altitude = level
    
# Button to land or go down
def land():
    global altitude, b1, b9
    altitude = -level

# Handler to draw the car position
def draw(canvas):
    global r1,r2, b1,b2,b3,b4,b5,b6,b7,b8,b9,fd1,fd2,fd3,fd4
    global bd1,bd2,bd3,bd4,fw,bw,h
    # draw label of the car on canvas
    canvas.draw_text("My simpleGUI car", [160,30], 20, "Orange")    
    # draw a blue line for the road, r
    canvas.draw_line(r1, r2, 5, "Blue")    
    # draw the main body of the car, b
    canvas.draw_polygon([b1,b2,b3,b4,b5,b6,b7,b8,b9], 1,"red", "red")
    # draw the front door window, fd
    canvas.draw_polygon([fd1,fd2,fd3,fd4],1,"orange", "yellow")
    # draw the back door window, bd
    canvas.draw_polygon([bd1,bd2,bd3,bd4],1, "orange", "yellow")
    #draw the front wheel, fw
    canvas.draw_circle(fw, 13, 1, "black", "black")
    # draw the back wheel, bw
    canvas.draw_circle(bw, 13, 1, "black", "black")
    # draw the head in the car, h
    canvas.draw_circle(h,6,1,"black", "black")
    canvas.draw_text(line1,[700,210], 10, "Orange")

#create frame and callbacks to event handlers
frame=simplegui.create_frame("My Frame", width, height)
frame.set_canvas_background("Brown")
frame.add_button("Forward",forward, 150)
frame.add_button("Reverse",reverse, 150)
frame.add_button("UP!", fly, 150)
frame.add_button("DOWN!", land, 150)
frame.add_button("Accelerate",accelerator, 150)
#frame.add_button("Decelerate",decelerator, 150)
frame.add_button("Emergency Brake", emergency_brake, 150)
frame.add_button("PARK THE CAR", park, 150)

#register draw handler
frame.set_draw_handler(draw)
#register timer
timer1=simplegui.create_timer(interval, tick_drive)

#start frame
frame.start()
timer1.start()


################################################
# THE STOPWATCH GAME
################################################
# template for "Stopwatch: The Game"

import simplegui
import time

# define global variables
interval= 100
tracker = 0
stops = 0
hits = 0
status="StopWatch"


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    # returns format A:BC.D
    if t <10:
        D = t % 10
        C = (t - D)/10
        B = 0
        A = 0
        return str(A)+":"+str(B)+str(C)+"."+str(D)
    elif t < 100:
        D = t % 10
        C = (t - D)/10
        B = (t - C*10- D)/60
        A = 0
        return str(A)+":"+str(B)+str(C)+"."+str(D)
    elif t <600:
        D = t % 10
        C = (t %100 - D)/10
        B = (t - C*10 -D)/100
        A = 0
        return str(A)+":"+str(B)+str(C)+"."+str(D)
    elif t >= 600:
        D = t % 10
        C = (t %100 - D)/10
        B = (t % 600 -D)/100
        A = (t - B*100 - C*10 -D)/600
        return str(A)+":"+str(B)+str(C)+"."+str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global tracker, hits, stops, status
    status="Watch running..."
    timer.start()

def stop():
    global tracker, hits, stops, status
    # check if timer running
    not_running = not timer.is_running()
    if not_running:
        status="Start watch first!"
    else:
        timer.stop()
        if float(tracker % 10) < 1:
            hits +=1
            stops += 1
            status=":-) Got'Em, Ha!"
        else:
            stops += 1
            status=":-(  You missed."
    

def reset():
    global tracker, hits, stops, status
    timer.stop()
    tracker = 0
    hits = 0
    stops = 0
    status = "StopWatch"

# define event handler for timer with 0.1 sec interval
def tick():
    global tracker
    tracker += 1
    #print tracker

# define draw handler
def draw(canvas):
    canvas.draw_polygon([[80,185],[80,140],[230,140],[230,185]],5, "black", "orange")
    canvas.draw_text(format(tracker), [95,180], 50, "black")
    canvas.draw_text(str(hits)+"/"+str(stops), [230,35],25, "white")
    canvas.draw_text(status, [20,35], 25, "yellow")
    canvas.draw_circle([155, 160],105,10,"black")
    
    
# create frame
frame=simplegui.create_frame("StopWatch",300,300)

# register event handlers
timer = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw)
frame.set_canvas_background("brown")
start = frame.add_button("START", start, 120)
stop = frame.add_button("STOP", stop, 120)
reset = frame.add_button("RESET", reset, 120)


# start frame
frame.start()

# Please remember to review the grading rubric

#--------------------------------------------------------------
# FINAL MINI PROJ WEEK 4: PONG
#--------------------------------------------------------------
# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
#LEFT = False
#RIGHT = True

direction = random.choice(['LEFT', 'RIGHT'])
ball_pos = [WIDTH / 2, HEIGHT / 2]
paddle1_vel = 0
paddle2_vel = 0
rules1 = "Instructions:"
rules2 = """
This is Pong!
This is a two-player game. However, 
if you have no friends, do not worry
because this is also a good opportunity to battle
your left hand vs. your right hand!
"""
rules3="""
Left controls:
Up 	 - 	'w'
Down -  's'
"""
rules4 ="""
Right Controls:
Up 	 - 	'up arrow'
Down -  'down arrow'
"""
rules5="""
Push RESTART to do just that. Enjoy!
"""
blank=" "

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    v_horiz = random.randrange(120, 140)
    v_vert = random.randrange(60, 180)
    
    if direction == 'LEFT':
        #spawn up and left
        ball_vel = [-v_horiz/60, -v_vert/60]
        
    elif direction == 'RIGHT':
        #spawn up and right
        ball_vel = [v_horiz/60, -v_vert/60]
    else:
        pass
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,direction  # these are numbers
    global score1, score2  # these are ints
    
    direction = random.choice(['LEFT', 'RIGHT'])
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    score1 = 0
    score2 = 0
    spawn_ball(direction)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel

    # draw mid line and gutters
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], 50, 1, 'white')
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
   
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS or ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[0]<=BALL_RADIUS + PAD_WIDTH and abs(ball_pos[1]-paddle1_pos) < HALF_PAD_HEIGHT + BALL_RADIUS:
        ball_vel[0] = -ball_vel[0] * 1.1
    elif ball_pos[0]>=WIDTH - 1 - BALL_RADIUS - PAD_WIDTH and abs(ball_pos[1]-paddle2_pos)< HALF_PAD_HEIGHT + BALL_RADIUS:
        ball_vel[0] = -ball_vel[0] * 1.1
    elif ball_pos[0] >= WIDTH - 1 - BALL_RADIUS - PAD_WIDTH:
        score1 += 1
        spawn_ball('LEFT')
    elif ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        score2 += 1
        spawn_ball('RIGHT')
    else:
        ball_vel[0] = ball_vel[0]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'white', 'white')
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if paddle1_pos <= HALF_PAD_HEIGHT or paddle1_pos >= HEIGHT - 1 - HALF_PAD_HEIGHT:
        paddle1_vel = 0
    if paddle2_pos <= HALF_PAD_HEIGHT or paddle2_pos >= HEIGHT - 1 - HALF_PAD_HEIGHT:
        paddle2_vel = 0
        
    # get ball speed
    speed ="Ball Speed: "+ str(abs(ball_vel[0]*60))+ " px/sec"
    
    # draw paddles
    canvas.draw_line([0,paddle1_pos + HALF_PAD_HEIGHT],[0, paddle1_pos - HALF_PAD_HEIGHT], PAD_WIDTH, 'yellow')
    canvas.draw_line([WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH, paddle2_pos - HALF_PAD_HEIGHT], PAD_WIDTH, 'yellow')
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 4, 50], 50, 'white')
    canvas.draw_text(str(score2), [3*WIDTH / 4, 50], 50, 'white')
    canvas.draw_text(speed, [WIDTH /2-100, HEIGHT], 15, 'yellow')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['up'] and paddle2_pos > HALF_PAD_HEIGHT:
        paddle2_vel -= 10
    elif key == simplegui.KEY_MAP['down'] and paddle2_pos<= HEIGHT - 1 - HALF_PAD_HEIGHT:
        paddle2_vel += 10
    elif key == simplegui.KEY_MAP['w'] and paddle1_pos > HALF_PAD_HEIGHT:
        paddle1_vel -= 10
    elif key == simplegui.KEY_MAP['s'] and paddle1_pos <= HEIGHT - 1 - HALF_PAD_HEIGHT:
        paddle1_vel += 10
    else:
        pass
   
def keyup(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    else:
        pass

def restart():
    new_game()
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_label(rules1, 210)
frame.add_label(blank, 210)
frame.add_label(rules2, 210)
frame.add_label(blank, 210)
frame.add_label(rules3, 210)
frame.add_label(blank, 210)
frame.add_label(rules4, 210)
frame.add_label(blank, 210)
frame.add_label(rules5, 210)
frame.add_label(blank, 210)
frame.add_button("RESTART", restart, 120)
# start frame
new_game()
frame.start()

