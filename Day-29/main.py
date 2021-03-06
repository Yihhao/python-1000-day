from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave fields empty!")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email} "
        #                                                       f"\nPassword: {password} \nIs it ok to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving update data
                json.dump(data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving update data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- FIND PASSEWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            email = data[website]["email"]
            password = data[website]["password"]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    except KeyError:
        messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    else:
        messagebox.showinfo(title=website, message=f"Email: {email} \nPassword:{password}")

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Manager")
windows.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

email_username_input = Entry(width=42)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "yihao0425@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Button
search_button = Button(text="Search", command=find_password)
search_button.config(highlightthickness=0, bg="white", width=17)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.config(highlightthickness=0, bg="white", width=17)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save)
add_button.config(width=36, highlightthickness=0, bg="white")
add_button.grid(column=1, row=4, columnspan=2)

windows.mainloop()
