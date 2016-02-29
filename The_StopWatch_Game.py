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