from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT = ("Courier", 10, "italic")
WHITE = "#f4f9f9"


def search_data():
    website_name = website_text.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No such data")
    else:
        if website_name in data:
            info_email = data[website_name]["Email"]
            info_password = data[website_name]["Password"]
            messagebox.showinfo(title=f"{website_name}",
                                message=f"Email:{info_email}\nPassword:{info_password}(copied)")
            pyperclip.copy(info_password)

        else:
            messagebox.showinfo(title="Error", message=f"{website_name} does not exits in data")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_number + password_symbol + password_letter

    shuffle(password_list)

    generated_password = "".join(password_list)
    password_text.delete(0, END)
    password_text.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    website_name = website_text.get()
    email = info_text.get()
    password_name = password_text.get()

    new_data = {
        website_name: {
            "Email": email,
            "Password": password_name
        }
    }

    if len(website_name) == 0 and len(password_name) == 0:
        messagebox.showinfo(title="oppss", message="Dont leave any area blank")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_text.delete(0, END)
            password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website = Label(text="Website:", bg=WHITE)
website.grid(row=1, column=0)

website_text = Entry(width=40)
website_text.focus()
website_text.grid(row=1, column=1, columnspan=2)

user_info = Label(text="Email/Username:", bg=WHITE)
user_info.grid(row=2, column=0)

info_text = Entry(width=40)

info_text.grid(row=2, column=1, columnspan=2)

password = Label(text="Password:", bg=WHITE)
password.grid(row=3, column=0)

password_text = Entry(width=30)
password_text.grid(row=3, column=1)

generate_btn = Button(text="Generate Password", width=18, bg=WHITE, command=generate_password)
generate_btn.grid(row=3, column=3)

add_btn = Button(text="Add", width=45, bg=WHITE, command=save_info)
add_btn.grid(row=4, column=1, columnspan=3)

search_btn = Button(text="Search", width=18, bg=WHITE, command=search_data)

search_btn.grid(row=1, column=3)

window.mainloop()
