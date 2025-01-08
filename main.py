from tkinter import *
from tkinter import Canvas, PhotoImage
import pandas as pd
import random


#you can call function inside function to loop
BACKGROUND_COLOR="#B1DDC6"

value=pd.read_csv("data/french_words.csv")
to_learn=value.to_dict(orient="records")
current_card={}
def next_card():
    global current_card
    current_card=random.choice(to_learn)

    #update the canvas with french word
    canvas.itemconfig(card_title, text="french", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    #to change in english every time
    window.after(3000,func=flip_card)

def flip_card():


    canvas.itemconfig(card_title, text="english")
    canvas.itemconfig(card_word, text=current_card["English"])


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#changing into eng
window.after(3000, func=flip_card)


canvas= Canvas(width=800, height=526)#same as a pic size
card_front_img=PhotoImage(file="images/card_front.png")
canvas.create_image(400,263, image= card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_title=canvas.create_text(400, 150, text="Title", font=("Ariel",40, "italic"))
card_word=canvas.create_text(400,263,text="", font=("Ariel", 40))
canvas.grid(row=0, column=0, columnspan=2)


cross_image= PhotoImage(file="images/wrong.png")
unknown_button=Button(image=cross_image, command= next_card)
unknown_button.grid(row=1, column=0)

checked_image= PhotoImage(file="images/right.png")
known_button=Button(image=checked_image, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()