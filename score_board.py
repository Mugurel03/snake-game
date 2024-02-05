from turtle import Turtle

ALIGN = 'center'
FONT = ('Calibri', 22, 'normal')


class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.color('White')
        self.penup()
        self.hideturtle()
        self.goto(0, 278)
        self.current_score = 0
        center = 'center'
        self.write("Score : " + str(self.current_score), True, align=ALIGN, font=FONT)

    def write_score(self):
        self.clear()
        self.write("Score : " + str(self.current_score), True, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', True, align=ALIGN, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.goto(0, 278)
        self.write_score()
