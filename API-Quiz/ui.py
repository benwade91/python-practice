from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quiz Game')
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", background=THEME_COLOR, foreground="white")
        self.score_label.grid(row=0, column=1, padx=20, pady=20,)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 207, text="Ready?",
                                                     width=250, font=("Arial", 20, "italic"), fill="white",
                                                     tag='question_text')
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.true_img = PhotoImage(file='images/true.png')
        self.true_btn = Button(image=self.true_img, highlightthickness=0)
        self.true_btn.grid(row=2, column=0, padx=20, pady=20,)

        self.false_img = PhotoImage(file='images/false.png')
        self.false_btn = Button(image=self.false_img, highlightthickness=0)
        self.false_btn.grid(row=2, column=1, padx=20, pady=20,)

        self.window.mainloop()
