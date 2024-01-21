from tkinter import Tk, Entry, Button, Label, Frame
import tkinter.font as tkFont
from mainLogic import organize_folder
top = Tk()
top.geometry("500x300")
top.title("Directory Organizer")

default_font = tkFont.Font(family="Helvetica", size=13)
big_font = tkFont.Font(family="Helvetica", size=14, weight="bold")

def retrieve_input():
    input_value = directory.get()
    organize_folder(input_value)
    result_label.config(text="All done!")
    result_label.pack(pady=(5, 10))
    print(input_value)

entry_frame = Frame(top)
entry_frame.pack(pady=20)

label = Label(entry_frame, text="Enter absolute path for directory:", font=default_font)
label.pack(side="top", fill="x")

directory = Entry(entry_frame, width=50, font=big_font)
directory.pack(side="top", pady=(5, 10))

submit = Button(entry_frame, text="Organize", command=retrieve_input, font=big_font)
submit.pack(side="top")

result_label = Label(top, text="", fg="green", font=big_font)

top.mainloop()
