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
