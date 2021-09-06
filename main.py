import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_forward()

    # Detect collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # When the turtle reaches finish line
    if player.ycor() >= 280:
        player.reset_position()
        car_manager.increase_car_speed()
        score_board.increase_score()
        score_board.update_scoreboard()


