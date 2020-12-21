import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_car:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful process
    if player.is_at_finishing_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.increase_speed()

screen.exitonclick()
