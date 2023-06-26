import sys
import os

g = os.path.abspath("Text_to_Speech_App")
print(g)
sys.path.append(g)

from Text_speech import Speak
from data import data
import tkinter as ttk
import random as rd


def Reader(txt, author):
    r = f'{txt} By {author}'
    # Speak(r)


root = ttk.Tk()
root.title("Quotes Generator")

root.attributes("-zoomed", True)

# This Function updates the quote using rand index

idx = 0


def update_quote():

    global idx
    idx += 1
    if idx > len(data)-1:
        idx = 0
    # idx = random.randint(0, len(data)-1)
    quote_label.config(text=data[idx]["content"])
    author_label.config(text=f"~{data[idx]['author']}")
    Reader(data[idx]["content"], data[idx]['author'])


frame = ttk.Frame(root)
frame.pack(padx=20, pady=40)
frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)

defaultText="Reality leaves a lot to the imagination."
defaultAuthor="John Lennon"
quote_label = ttk.Label(frame, text=defaultText, font=(
    "Helvetica", 16), wraplength=550)
quote_label.pack()

author_label = ttk.Label(frame, text=f"~{defaultAuthor}", font=("Helvetica", 12))
author_label.pack(pady=10)


ttk.Button(frame, text="Get Quote", command=(update_quote)).pack(padx=20)

root.mainloop()
