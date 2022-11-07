from tkinter import *
import pandas
import random

FONT = "Courier", 25, "normal"
FONT_WORD = "Courier", 60, "normal"
COLOR_BG = "#252325"
COLOR_TEXT = "#fcffc0"
COLOR_FRONT_CARD = "#ee9c5d"
COLOR_BACK_CARD = "#2979b2"

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original = pandas.read_csv("geo_bel.csv")
    to_learn = original.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card
    global flip_timer
    win.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    can.itemconfig(mova, text="ქართული ენა", fill=COLOR_TEXT)
    can.itemconfig(slova, text=current_card["Georgian"], fill=COLOR_TEXT)
    can.itemconfig(background, image=front_image)
    flip_timer = win.after(3000, func=flip_card)
    x_button.config(image=x_image)
    v_button.config(image=v_image)

def flip_card():
    can.itemconfig(mova, text="Bielaruskaja", fill=COLOR_TEXT)
    can.itemconfig(slova, text=current_card["Belarusian"], fill=COLOR_TEXT)
    #For the Latin alphabet replace "Belarusian" with "Kryvian"
    can.itemconfig(background, image=back_image)
    x_button.config(image=x_image_fliped)
    v_button.config(image=v_image_fliped)

def known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()

win = Tk()
win.title ("Kartki")
win.config(padx=0, pady=0, bg=COLOR_BG)

flip_timer = win.after(3000, func=flip_card)

can = Canvas(width=800, height=600)
front_image = PhotoImage(file="./images/front_card.png")
back_image = PhotoImage(file="./images/back_card.png")
background = can.create_image(400, 300, image=front_image)
mova = can.create_text(400, 205, text="", font=FONT, fill=COLOR_TEXT)
slova = can.create_text(400, 250, text="", font=FONT_WORD, fill=COLOR_TEXT)
can.config(bg=COLOR_BG, highlightthickness=0)
can.pack()

x_image = PhotoImage(file="./images/x_button.png")
x_image_fliped =PhotoImage(file="./images/x_button_f.png")
x_button = Button(image=x_image, highlightthickness=0, command=next_card)
x_button.place(x=160, y=350)

v_image = PhotoImage(file="./images/v_button.png")
v_image_fliped =PhotoImage(file="./images/v_button_f.png")
v_button = Button(image=v_image, highlightthickness=0, command=known)
v_button.place(x=520, y=350)


next_card()

win.mainloop()