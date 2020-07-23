import turtle
import os


class Paddle(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color("burlywood")
        self.penup()
        self.setposition(x, y)
        self.shapesize(5, 1)  # factor of; default size is 20x20

    def up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)


class Ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()

        self.dx = 3
        self.dy = 3

    def move(self):
        self.setposition(self.xcor() - self.dx, self.ycor() - self.dy)


# game window
wn = turtle.Screen()
wn.title("jPong")
wn._bgcolor("SeaGreen")
wn.setup(800, 600)
wn.tracer

# set up
paddle_l = Paddle(-350, 0)
paddle_r = Paddle(350, 0)
ball = Ball()
score_l = 0
score_r = 0

# keyboard binding
wn.listen()
wn.onkeypress(paddle_l.up, "w")
wn.onkeypress(paddle_l.down, "s")
wn.onkeypress(paddle_r.up, "Up")
wn.onkeypress(paddle_r.down, "Down")

if __name__ == "__main__":
    while True:
        wn.update()

        # move the ball
        ball.move()
        # print(ball.position())
        # boarder/hit checking

        # top
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        # bottom
        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # left
        elif ball.xcor() < -390:
            score_r += 1
            ball.setposition(0, 0)
            ball.dx *= -1

        # right
        elif ball.xcor() > 390:
            score_l += 1
            ball.setposition(0, 0)
            ball.dx *= -1

        # left paddle
        elif ball.xcor() == -330 and paddle_l.ycor() - 60 <= ball.ycor() <= paddle_l.ycor() + 60:   # ball.xcor() == -330 rather than < to avoid the condition passing after ball has passed the paddle and cause glitch/shutter
            ball.dx *= -1

        # right paddle
        elif ball.xcor() == 330 and paddle_r.ycor() - 60 <= ball.ycor() <= paddle_r.ycor() + 60:
            ball.dx *= -1
