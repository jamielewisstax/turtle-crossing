from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.hideturtle()
        self.goto(-215, 260)
        self.color("black")
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.write(arg=f"Level: {self.current_level}", align=ALIGNMENT, font=FONT)
        self.current_level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
