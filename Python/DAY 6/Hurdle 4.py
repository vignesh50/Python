    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
def jump():
    turn_left()
    while wall_on_right():
        move()
    if right_is_clear():
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        turn_left()
    else:
        while wall_on_right():
            turn_left()
            move()
            turn_right()

        
while at_goal() != True:
    if front_is_clear():
        move()
    else:
        jump()
       
       
       

   



   



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
