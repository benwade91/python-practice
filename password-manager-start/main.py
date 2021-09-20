from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40)

lock_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, columnspan=2, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.focus()
email_input.grid(column=1, columnspan=2, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.focus()
password_input.grid(column=1, row=3)

generate_btn = Button(text='Generate Password')
generate_btn.grid(column=2, row=3)

add_btn = Button(text='Add', width=36)
add_btn.grid(column=1, columnspan=2, row=4)

window.mainloop()