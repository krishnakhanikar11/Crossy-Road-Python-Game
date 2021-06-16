from turtle import Screen
from ourMove import Our
from car import Car
import time
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Crossy Road')
screen.tracer(0)

score = Score()
our_turtle = Our()


screen.listen()
screen.onkey(our_turtle.move, "Up")

car = Car()

is_on_game = True

while is_on_game:
    time.sleep(0.15)
    screen.update()
    car.create_car()
    car.move_car()

    if our_turtle.ycor()> 290:
        our_turtle.res()
        score.updateLevel()
        car.level_up()

    for cars in car.all_cars:
        if cars.distance(our_turtle) < 20:
            screen.clear()
            score.finalLevel()
            is_on_game = False

screen.exitonclick()