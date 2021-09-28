from tkinter import *
from tkinter import messagebox
import time
import pandas
from flash_card_model import FlashCard
from game_brain_model import GameBrain

BACKGROUND_COLOR = "#B1DDC6"


flash_cards = []

# ------------------GAME CLASSES----------------- #


# ------------------GAME DATA----------------- #
with open('data/french_words.csv') as french_csv:
    french_data = pandas.read_csv(french_csv)
    french_dic = {row.French: row.English for (index, row) in french_data.iterrows()}

# ------------------START GAME----------------- #
def start_game():
    # time.sleep(5)
    canvas.create_image(400, 265, image=eng_window)
    canvas.create_text(400, 265, font="Times 20 italic bold", text='words')
    for (french, english) in french_dic.items():
        new_card = FlashCard(french, english)
        flash_cards.append(new_card)
    print(flash_cards)
    game = GameBrain(right_img, wrong_img)

# ------------------WINDOW----------------- #
window = Tk()
window.title('Flash-Game')
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
french_window = PhotoImage(file='images/card_front.png')
eng_window = PhotoImage(file='images/card_back.png')
right_img = PhotoImage(file='images/right.png')
wrong_img = PhotoImage(file='images/wrong.png')
canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.config(background=BACKGROUND_COLOR)
canvas.create_image(400, 265, image=french_window)
canvas.grid(column=0, row=0, columnspan=2)


begin_game = messagebox.askokcancel(title="Welcome", message="Ready to begin?")

if begin_game:
    start_game()

window.mainloop()