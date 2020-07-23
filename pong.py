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
        self.shape("circle")
        self.color("white")
        self.penup()

        self.dx = 10
        self.dy = 10

    def move(self):
        self.setposition(self.xcor() - self.dx, self.ycor() - self.dy)


# game window
wn = turtle.Screen()
wn.title(" Pong")
wn._bgcolor("SeaGreen")
wn.setup(800, 600)
wn.tracer

# scoreboard
sb = turtle.Turtle()
sb.speed(0)
sb.color("white")
sb.penup()
sb.hideturtle()
sb.setposition(0, 260)
sb.write("Player One: 0            Player Two: 0", align="center", font=("Comic Sans MS", 22, "normal"))

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

        while score_l < 3 and score_r < 3:
            # move the ball
            ball.move()

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
                sb.clear()
                sb.write(f"Player One: {score_l}            Player Two: {score_r}", align="center", font=("Comic Sans MS", 22, "normal"))
                ball.setposition(0, 0)
                ball.dx *= -1

            # right
            elif ball.xcor() > 390:
                score_l += 1
                sb.clear()
                sb.write(f"Player One: {score_l}            Player Two: {score_r}", align="center", font=("Comic Sans MS", 22, "normal"))
                ball.setposition(0, 0)
                ball.dx *= -1

            # left paddle
            elif paddle_l.ycor() - 50 <= ball.ycor() <= paddle_l.ycor() + 50 and -350 < ball.xcor() <= -330:
                ball.setx(-330)
                ball.dx *= -1

            # right paddle
            elif paddle_r.ycor() - 50 <= ball.ycor() <= paddle_r.ycor() + 50 and 350 > ball.xcor() >= 330:
                ball.setx(330)
                ball.dx *= -1

        if score_l == 3 or score_r == 3:
            sb.clear()
            score_l += 10   # to avoid repeating clear and write
            score_r += 10
            sb.write("Game Over", align="center", font=("Comic Sans MS", 22, "normal"))
            print("over")
