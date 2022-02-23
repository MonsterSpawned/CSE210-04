# Kent Lewis
import turtle

class Player():
    
    def __init__(self):
        self.player_color = "green"
        self.player_shape = "square"
        self.player_speed = 10
        self.player_body = turtle.Turtle()
        self.player_body.penup()
        self.player_body.color(self.player_color)
        self.player_body.shape(self.player_shape)
        self.player_body.sety(-250)

    def move_right(self):
        self.player_body.forward(self.player_speed)

    def move_left(self):
        self.player_body.right(180)
        self.player_body.forward(self.player_speed)
        self.player_body.right(180)