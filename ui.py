import tkinter
from quiz_brain import *

THEME_COLOR = "#375362"

class UI():
    SCORE_CORRECT = 0
    SCORE_WRONG = 0
    SCORE_TEXT = f"Score {SCORE_CORRECT}/{SCORE_WRONG}"
    def __init__(self,quiz_game: QuizBrain):
        self.quiz = quiz_game
        self.quiz_window = tkinter.Tk()
        self.quiz_window.title("Quiz game")
        self.quiz_window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = tkinter.Label(text=UI.SCORE_TEXT, fg="white", bg=THEME_COLOR)
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
        self.quiz_canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.quiz_canvas.itemconfig(self.question_text, text=q_text)
    def user_answer_true(self):
        is_true = self.quiz.check_answer(user_answer='True')
        self.feedback(is_true)

    def user_answer_wrong(self):
        is_true = self.quiz.check_answer(user_answer='False')
        self.feedback(is_true)

    def feedback(self, signal):
        if signal:
            self.quiz_canvas.config(bg='green')
        else:
            self.quiz_canvas.config(bg='red')
        self.quiz_window.after(1000, self.get_next_question)




