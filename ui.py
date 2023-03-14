import tkinter
from quiz_brain import *

THEME_COLOR = "#375362"

class UI():
    def __init__(self,quiz_game: QuizBrain):
        self.quiz = quiz_game
        self.quiz_window = tkinter.Tk()
        self.quiz_window.title("Quiz game")
        self.quiz_window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = tkinter.Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.quiz_canvas = tkinter.Canvas(width=300, height=250, bg='white')
        self.question_text = self.quiz_canvas.create_text(
            150,
            125,
            width=200,
            text="some question text here",
            fill=THEME_COLOR,
            font=("Arial", 15)
        )
        self.quiz_canvas.grid(row=1, column=0, columnspan=2)

        correct_image = tkinter.PhotoImage(file="images/true.png")
        wrong_image = tkinter.PhotoImage(file="images/false.png")

        self.correct_button = tkinter.Button(image=correct_image, command=self.user_answer_true)
        self.correct_button.grid(row=2,column=0, pady=50)

        self.wrong_button = tkinter.Button(image=wrong_image, command=self.user_answer_wrong)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()


        self.quiz_window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.quiz_canvas.itemconfig(self.question_text, text=q_text)
    def user_answer_true(self):
        self.quiz.check_answer(user_answer=True)

    def user_answer_wrong(self):
        self.quiz.check_answer(user_answer=False)

