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

