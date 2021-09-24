import json
from tkinter import *
from tkinter import messagebox
import random
import re
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '@', '#', '$', '&', '?']

    password_letters = [random.choice(letters) for x in range(random.randint(6, 8))]
    password_numbers = [random.choice(numbers) for x in range(random.randint(1, 3))]
    password_symbols = [random.choice(symbols) for x in range(random.randint(1, 3))]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = ''.join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, string=password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0:
        messagebox.showerror(title='Invalid Website', message='Please enter a website name')

    elif not validate_email(email):
        messagebox.showerror(title='Invalid Email', message='Please enter a valid email')

    elif len(password) == 0:
        messagebox.showerror(title='Invalid Password', message='Please enter a password')

    else:
        confirm_info = messagebox.askokcancel(title=website, message=f"email: {email} \n "
                                                                     f"password: {password} \n is this correct?")
        json_data = {
            website: {
                "email": email,
                "password": password
            }
        }
        if confirm_info:
            pw_file = open('passwords.json', 'w')
            json.dump(json_data, pw_file, indent=4)
            pw_file.close()
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)


def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return True
    else:
        return False

# ----------------------------LOAD CREDENTIALS ------------------------ #
def load_info():
    website = website_input.get()
    print(website)
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

website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=1, row=1)

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

load_btn = Button(text='Load Credentials', command=load_info)
load_btn.grid(column=2, row=1)

generate_btn = Button(text='Generate Password', command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(text='Add', width=36, command=save_password)
add_btn.grid(column=1, columnspan=2, row=4)

window.mainloop()