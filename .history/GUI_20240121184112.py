from tkinter import Tk, Entry, Button, Label, Frame
import tkinter.font as tkFont

top = Tk()
top.geometry("500x300")
top.title("Directory Organizer")

# Define a font
default_font = tkFont.Font(family="Helvetica", size=12)
big_font = tkFont.Font(family="Helvetica", size=14, weight="bold")

def retrieve_input():
    input_value = directory.get()
    result_label.config(text="All done!")
    result_label.pack(pady=(5, 10))
    print(input_value)

# Frame for Entry and Button
entry_frame = Frame(top)
entry_frame.pack(pady=20)

# Create a label for the entry field and pack it in the frame
label = Label(entry_frame, text="Enter absolute path for directory:", font=default_font)
label.pack(side="top", fill="x")

# Set the width of the Entry widget, apply the bigger font, and pack it in the frame
directory = Entry(entry_frame, width=50, font=big_font)
directory.pack(side="top", pady=(5, 10))

# Button that will pack in the frame under the Entry, with a bigger font
submit = Button(entry_frame, text="Organize", command=retrieve_input, font=big_font)
submit.pack(side="top")

# Label for displaying the result message, with a bigger font
result_label = Label(top, text="", fg="green", font=big_font)  # Initially empty

top.mainloop()
