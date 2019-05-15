import time
import os
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from random import randint

sense = SenseHat()

# colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# vars
ingame = 1
apple_X = 0
apple_Y = 0
apple_eated = 0
direction = 0
snake_X = [4,4,4]
snake_Y = [4,5,6]

# functions
def snake_reset():
    global apple_eated
    global direction
    global snake_X
    global snake_Y
    apple_eated = 0
    direction = 0
    snake_X = [4,4,4]
    snake_Y = [4,5,6]


def pushed_up(event):
    global direction
    if event.action != ACTION_RELEASED:
        if direction != 180:
            direction = 0
def pushed_down(event):
    global direction
    if event.action != ACTION_RELEASED:
        if direction != 0:
            direction = 180
def pushed_left(event):
    global direction
    if event.action != ACTION_RELEASED:
        if direction != 90:
            direction = 270
def pushed_right(event):
    global direction
    if event.action != ACTION_RELEASED:
        if direction != 270:
            direction = 90

def move_left ():
    if snake_X[0] < 1:
        snake_X.insert(0, 7)
    else:
        snake_X.insert(0, snake_X[0]-1)
    snake_Y.insert(0, snake_Y[0])
    return

def move_right ():
    if snake_X[0] > 6:
        snake_X.insert(0, 0)
    else:
        snake_X.insert(0, snake_X[0]+1)
    snake_Y.insert(0, snake_Y[0])
    return

def move_up ():
    if snake_Y[0] < 1:
        snake_Y.insert(0, 7)
    else:
        snake_Y.insert(0, snake_Y[0]-1)
    snake_X.insert(0, snake_X[0])
    return

def move_down ():
    if snake_Y[0] > 6:
        snake_Y.insert(0, 0)
    else:
        snake_Y.insert(0, snake_Y[0]+1)
    snake_X.insert(0, snake_X[0])
    return

def move_snake ():
    if direction == 0:
        move_up()
    elif direction == 90:
        move_right()
    elif direction == 180:
        move_down()
    elif direction == 270:
        move_left()

def pop_apple ():
    global apple_X
    global apple_Y
    global apple_eated
    apple_X = randint(0,7)
    apple_Y = randint(0,7)
    apple_eated = 0
    return

def draw_snake ():
    for i in range(0,len(snake_X)):
        if i == 0:
            sense.set_pixel(snake_X[i],snake_Y[i],blue)
        else:
            sense.set_pixel(snake_X[i],snake_Y[i],red)

def draw_apple():
    if apple_eated == 1:
        pop_apple()
    else:
        sense.set_pixel(apple_X,apple_Y,green)

def grow_snake():
    if apple_eated == 0:
        sense.set_pixel(snake_X[len(snake_X)-1],snake_Y[len(snake_Y)-1],0,0,0)
        del snake_X[-1]
        del snake_Y[-1]
    return

def collision_snakeApple():
    global apple_eated
    if snake_X[0] == apple_X:
        if snake_Y[0] == apple_Y:
            apple_eated = 1
    return

def collision_snakeSnake():
    global ingame
    for i in range(1,len(snake_X)):
        if snake_X[0] == snake_X[i]:
            if snake_Y[0] == snake_Y[i]:
                for j in range(0,10):
                    all_to_red()
                    time.sleep(0.1)
                    clear_all()
                    time.sleep(0.1)
                all_to_red()
                sense.show_message("=> ")
                sense.show_message(str(len(snake_X)))
                highscores = open(".snake","r")
                if int(highscores.read()) < len(snake_X):
                    highscores.close()
                    highscores = open(".snake","w")
                    highscores.write(str(len(snake_X)))
                    sense.show_message("HIGHSCORE")
                highscores.close()
                ingame = 0

def clear_all():
    for i in range(0,8):
        for j in range(0,8):
            sense.set_pixel(i,j,0,0,0)
    return

def all_to_red():
    for i in range(0,8):
        for j in range(0,8):
            sense.set_pixel(i,j,red)
    return

# main loop

if os.stat(".snake").st_size == 0:
    highscores = open(".snake","w")
    highscores.write("3")
    highscores.close()

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
while 1 :
    sense.show_message("Snake")
    clear_all()
    pop_apple()
    ingame = 1
    snake_reset()
    while ingame == 1 :
        move_snake()
        collision_snakeApple()
        collision_snakeSnake()
        if ingame == 1:
            grow_snake()
            draw_snake()
            draw_apple()
        delay = float(1)-float(float(len(snake_X))/float(15))
        if delay > 0.2:
            time.sleep(delay)
        else:
            time.sleep(0.2)
    

#sense.show_message("Hello, world!")
