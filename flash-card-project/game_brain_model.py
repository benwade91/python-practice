from tkinter import Button
import time

def test_print():
    print('it works')


class GameBrain:
    def __init__(self, right_img, wrong_img, flash_cards, canvas, eng_window, french_window):
        self.canvas = canvas
        self.eng_window = eng_window
        self.french_window = french_window
        self.right_button = Button(image=right_img, width=100, height=100, highlightthickness=0, command=self.correct)
        self.right_button.grid(column=1, row=1)
        self.wrong_button = Button(image=wrong_img, width=100, height=99, highlightthickness=0, command=self.incorrect)
        self.wrong_button.grid(column=0, row=1)
        self.flash_cards = flash_cards
        self.turn = 0

    def questions_left(self):
        return len(self.flash_cards) > self.turn

    def next_card(self):
        self.canvas.create_image(400, 265, image=self.eng_window)
        self.canvas.create_text(400, 265, font="Times 40 bold", text=self.flash_cards[self.turn].french)
        self.canvas.update()

        time.sleep(3)

        self.canvas.create_image(400, 265, image=self.french_window)
        self.canvas.create_text(400, 265, font="Times 40 bold", text=self.flash_cards[self.turn].english)
        self.canvas.update()

    def correct(self):
        self.flash_cards.remove(self.flash_cards[self.turn])
        print(len(self.flash_cards))
        self.next_card()

    def incorrect(self):
        self.turn += 1
        print(len(self.flash_cards))
        self.next_card()
