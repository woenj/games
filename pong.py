import turtle
import os


class Paddle:
    def __init__(self, x, y):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("burlywood")
        self.paddle.penup()
        self.paddle.setposition(x, y)
        self.paddle.shapesize(5, 1)  # factor of; default size is 20x20

    def up(self):
        y = self.paddle.ycor()
        y += 20
        self.paddle.sety(y)

    def down(self):
        y = self.paddle.ycor()
        y -= 20
        self.paddle.sety(y)


class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()


# game window
wn = turtle.Screen()
wn.title("jPong")
wn._bgcolor("DarkGreen")
wn.setup(800, 600)
wn.tracer

# set up
paddle_l = Paddle(-350, 0)
paddle_r = Paddle(350, 0)
ball = Ball()

# keyboard binding
wn.listen()
wn.onkeypress(paddle_l.up, "w")
wn.onkeypress(paddle_l.down, "s")
wn.onkeypress(paddle_r.up, "Up")
wn.onkeypress(paddle_r.down, "Down")

if __name__ == "__main__":
    while True:
        wn.update()
