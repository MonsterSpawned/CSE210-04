# Aitana
import turtle

class GameUtils():
    
    def __init__(self):
        self.currentScore = 0
        self.game_name = "Gem and Rock Game"
    
    def draw_text_to_screen(self, text_var, x_var, y_var):
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(x_var, y_var)
        pen.write(text_var, align="center",
                font=("candara", 24, "bold"))
        
    def get_score(self):
        return self.currentScore
    
    def set_score(self, score_var):
        self.currentScore = score_var
        
    def get_game_name(self):
        return self.game_name