from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brian: QuizBrain):
        self.quiz = quiz_brian

        self.windows = Tk()
        self.windows.title("Quizzler")
        self.windows.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=200,
            text="Some question test",
            fill=THEME_COLOR,
            font=("Arial", 18, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_figure = PhotoImage(file="images/true.png")
        self.true_button = Button(text="True", image=true_figure, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        false_figure = PhotoImage(file="images/false.png")
        self.false_button = Button(text="False", image=false_figure, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.windows.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.windows.after(1000, self.get_next_question)
