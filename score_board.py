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
        self.highest_score = self.read_highest_score()
        self.write("Score : " + str(self.current_score) + " Highest Score: " + str(self.highest_score), True,
                   align=ALIGN,
                   font=FONT)

    def write_score(self):
        self.clear()
        self.write("Score : " + str(self.current_score) + " Highest Score: " + str(self.highest_score), True,
                   align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', True, align=ALIGN, font=FONT)

    def increase_score(self):
        self.current_score += 1
        if self.current_score > self.highest_score:
            self.highest_score = self.current_score
            self.update_highest_score()
        self.goto(0, 278)
        self.write_score()

    def read_highest_score(self):
        with open("data.txt", "r") as file:
            return int(file.read())

    def update_highest_score(self):
        with open("data.txt", "w") as file:
            file.write(str(self.highest_score))
