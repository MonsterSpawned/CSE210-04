# Kent Lewis
import turtle

class Player():
    
    def __init__(self):
        self.player_color = "green"
        self.player_shape = "square"
        self.player_speed = 1
        self.player_body = turtle.Turtle()
        self.player_body.color(self.player_color)
        self.player_body.shape(self.player_shape)
        self.player_body.goto(0,0)