from tkinter.simpledialog import askstring
from tkinter import *
top = Tk()
top.geometry("500x300")

def retrieve_input():
    input_value = directory.get()
    print(input_value)
top_label = Label(top,str="Input the absolute path")
directory = Entry(top)
directory.pack()
top_label.pack()
submit = Button(top, text ="Organize", command = retrieve_input)
submit.place(x=50,y=50)
top.mainloop()
