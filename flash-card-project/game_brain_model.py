from tkinter import Button
import time
import os.path
import pandas
import csv

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
        try:
            self.canvas.create_image(400, 265, image=self.eng_window)
            self.canvas.create_text(400, 200, font="Times 40 italic", text="french", tags=('french',))
            self.canvas.create_text(400, 265, font="Times 40 bold", text=self.flash_cards[self.turn].french)
            self.canvas.update()

            time.sleep(3)

            self.canvas.create_image(400, 265, image=self.french_window)
            self.canvas.create_text(400, 200, font="Times 40 italic", text="english")
            self.canvas.create_text(400, 265, font="Times 40 bold", text=self.flash_cards[self.turn].english)
            self.canvas.update()

        except IndexError:
            self.canvas.delete('french')
            self.canvas.create_text(400, 200, font="Times 40 italic", text="Game Over")
            self.canvas.create_text(400, 265, font="Times 40 bold", text="That's all of them!")
            self.canvas.update()

    def correct(self):
        self.remove_learned_word()
        self.flash_cards.remove(self.flash_cards[self.turn])
        print(len(self.flash_cards))
        self.next_card()

    def incorrect(self):
        print(len(self.flash_cards))
        self.words_to_learn()
        self.turn += 1
        self.next_card()

    def words_to_learn(self):
        if os.path.exists('data/words_to_learn.csv'):
            with open('data/words_to_learn.csv', 'a') as wtl:
                if self.flash_cards[self.turn].french:
                    print(True)
                else:
                    print(False)
                wtl.write(f'{self.flash_cards[self.turn].french},{self.flash_cards[self.turn].english}\n')
        else:
            with open('data/words_to_learn.csv', 'a') as wtl:
                wtl.write('French,English\n')
                wtl.write(f'{self.flash_cards[self.turn].french},{self.flash_cards[self.turn].english}\n')

    def remove_learned_word(self):
        if os.path.exists('data/words_to_learn.csv'):
            with open('data/words_to_learn.csv') as french_csv:
                french_data = pandas.read_csv(french_csv)
                print(french_data)
                french_data = french_data[french_data.French != self.flash_cards[self.turn].french]
                print(french_data)
                french_data.to_csv('data/words_to_learn.csv', index=False)
