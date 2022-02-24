# Aitana
import turtle


class GameUtils:
    def __init__(self):
        self.currentScore = 0
        self.game_name = "Gem and Rock Game"

    def draw_text_to_screen(self, text_var: str, x_var: int, y_var: int):
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(x_var, y_var)
        pen.write(text_var, align="center", font=("candara", 24, "bold"))

    def get_score(self):
        return self.currentScore

    def set_score(self, score_var: int):
        self.currentScore = score_var

    def get_game_name(self):
        return self.game_name
