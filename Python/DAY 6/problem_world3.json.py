def turn_right():
    turn_left()
    turn_left()
    turn_left()
right_count = 0
while at_goal() != True:
    if right_is_clear():
        turn_right()
        move()
        right_count += 1
        if right_count > 6:
            while front_is_clear():
                move()
    elif front_is_clear():
        move()
    else:
        turn_left()
       

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
