from tkinter import Tk, Entry, Button, Label

top = Tk()
top.geometry("500x300")

def retrieve_input():
    input_value = directory.get()
    result_label = Label(top, text="All done!")
    result_label.place(x=50, y=110)  # Place the label below the button

    print(input_value)

# Create a label for the entry field
label = Label(top, text="Enter absolute path for directory:")
label.place(x=50, y=0)

# Set the width of the Entry widget to 100 characters
directory = Entry(top, width=100)
directory.place(x=50, y=50)  # Adjust y to place it below the label

submit = Button(top, text="Organize", command=retrieve_input)
submit.place(x=50, y=80)  # Adjust y to place it below the entry field

top.mainloop()
