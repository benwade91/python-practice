from tkinter import Button


def test_print():
    print('it works')


class GameBrain:
    def __init__(self, right_img, wrong_img):
        self.right_button = Button(image=right_img, width=100, height=100, highlightthickness=0, command=test_print)
        self.right_button.grid(column=1, row=1)
        self.wrong_button = Button(image=wrong_img, width=100, height=99, highlightthickness=0, command=test_print)
        self.wrong_button.grid(column=0, row=1)
