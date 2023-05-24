import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#class from player file
plR = Player()

#class from carManager file
cmR = CarManager()

#class from scorebaord file
sbR = Scoreboard()

#screen listening for keystrokes
screen.listen()
screen.onkey(plR.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #To create a new car after every sleep,update and refresh
    cmR.create_car()
    #method from car manager which makes car to move
    cmR.move_cars()

    #Detecting collision with car
    for cars in cmR.all_cars:
        if cars.distance(plR) < 20:
            game_is_on = False
            sbR.game_over()

    #Detecting a successful crossing and increase the level
    if plR.finish_line():
        plR.goto_start()
        cmR.level_up()
        sbR.increase_level()






screen.exitonclick()