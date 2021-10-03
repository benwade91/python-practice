from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Quiz Game')
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", background=THEME_COLOR, foreground="white")
        self.score_label.grid(row=0, column=1, padx=20, pady=20, )

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Ready?",
                                                     width=280, font=("Arial", 20, "italic"), fill="black",
                                                     tag='question_text')
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.true_img = PhotoImage(file='images/true.png')
        self.true_btn = Button(image=self.true_img, highlightthickness=0, command=self.true_answer)
        self.true_btn.grid(row=2, column=0, padx=20, pady=20, )

        self.false_img = PhotoImage(file='images/false.png')
        self.false_btn = Button(image=self.false_img, highlightthickness=0, command=self.false_answer)
        self.false_btn.grid(row=2, column=1, padx=20, pady=20, )

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            print(question)
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your final score is {self.quiz.score}/10")

    def true_answer(self):
        answer = self.quiz.check_answer("True")
        self.ui_feedback(answer)

    def false_answer(self):
        answer = self.quiz.check_answer("False")
        self.ui_feedback(answer)

    def ui_feedback(self, answer):
        if answer:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)

