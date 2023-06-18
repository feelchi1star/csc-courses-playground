import tkinter as ttk
from data import data
root = ttk.Tk()
root.title("Quotes Generator")
# root.geometry("700x250")
root.attributes("-zoomed", True)


def update_quote():
    print(len(data))
    quote_label.config(text="asjkdlsjlakd")


frame = ttk.Frame(root, bg="red")
frame.pack(padx=30, pady=40)
frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)

quote_label = ttk.Label(frame, text="", font=("Helvetica", 16), wraplength=650)
quote_label.pack()

author_label = ttk.Label(frame, text="", font=("Helvetica", 12))
author_label.pack(pady=10)


ttk.Button(frame, text="Get Quote", command=update_quote).pack(padx=20)

root.mainloop()
