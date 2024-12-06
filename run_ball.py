import turtle
import ball
import random

class Simulator:
    def __init__(self, num_balls):
        self.num_balls = num_balls
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)
        ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []

        # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
        for i in range(self.num_balls):
            self.xpos.append(random.uniform(-1*self.canvas_width + ball_radius, self.canvas_width - ball_radius))
            self.ypos.append(random.uniform(-1*self.canvas_height + ball_radius, self.canvas_height - ball_radius))
            self.vx.append(10*random.uniform(-1.0, 1.0))
            self.vy.append(10*random.uniform(-1.0, 1.0))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)


S = Simulator(5)
dt = 0.2 # time step
while (True):
    turtle.clear()
    S.draw_border()
    for i in range(S.num_balls):
        ball.Ball.draw_ball()
        ball.Ball.move_ball(dt)
        ball.Ball.update_ball_velocity()
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()

