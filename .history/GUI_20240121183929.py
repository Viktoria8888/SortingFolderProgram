from tkinter import Tk, Entry, Button, Label, Frame

top = Tk()
top.geometry("500x300")
top.title("Directory Organizer")

def retrieve_input():
    input_value = directory.get()
    result_label.config(text="All done!")
    result_label.pack(pady=(5, 10))  # Add some padding above and below the label
    print(input_value)

# Frame for Entry and Button
entry_frame = Frame(top)
entry_frame.pack(pady=20)

# Create a label for the entry field and pack it in the frame
label = Label(entry_frame, text="Enter absolute path for directory:")
label.pack(side="top", fill="x")

# Set the width of the Entry widget and pack it in the frame
directory = Entry(entry_frame, width=50)
directory.pack(side="top", pady=(5, 10))

# Button that will pack in the frame under the Entry
submit = Button(entry_frame, text="Organize", command=retrieve_input)
submit.pack(side="top")

# Label for displaying the result message
result_label = Label(top, text="", fg="green")  # Initially empty and green colored text

top.mainloop()
