from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    datafile = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_datafile = pandas.read_csv("./data/french_words.csv")
    to_lean = original_datafile.to_dict(orient="records")
else:
    to_lean = datafile.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    windows.after_cancel(flip_timer)
    current_card = random.choice(to_lean)
    canvas.itemconfig(card_title, text=f"French", fill="black")
    canvas.itemconfig(card_word, text=f"{current_card['French']}", fill="black")
    flip_timer = canvas.itemconfig(card_background, image=card_front_image)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(card_title, text=f"English", fill="white")
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill="white")


def is_known():
    to_lean.remove(current_card)
    data = pandas.DataFrame(to_lean)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


windows = Tk()
windows.title("Flashy")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = windows.after(3000, flip_card)

# Image
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button
cross_image = PhotoImage(file="images/wrong.png")
unknown_image = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_image.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_image = Button(image=check_image, highlightthickness=0, command=is_known)
known_image.grid(column=1, row=1)

next_card()

windows.mainloop()
