from tkinter.simpledialog import askstring
from tkinter import *
top = Tk()
top.geometry("1080x720")
def retrieve_input():
    input_value = directory.get()
    print(input_value)

directory = Entry(top)
directory.pack()
submit = Button(top, text ="Organize", command = retrieve_input)
submit.place(x=50,y=50)
top.mainloop()
