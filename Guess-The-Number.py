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
