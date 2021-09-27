from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flash-Game')
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
french_window = PhotoImage(file='images/card_front.png')
eng_window = PhotoImage(file='images/card_back.png')
canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.config(background=BACKGROUND_COLOR)
canvas.create_image(400, 265, image=french_window)
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img, width=100, height=100, highlightthickness=0)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img, width=100, height=99, highlightthickness=0)
wrong_button.grid(column=0, row=1)



window.mainloop()