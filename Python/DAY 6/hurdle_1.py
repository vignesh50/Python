
def jump():
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

for x in range(0,6):
    move()
    turn_left()
    jump()

