
from tkinter import *

root = Tk()
root.geometry("633x422")
def resize():
    width_value = width.get()
    height_value = height.get()
    root.geometry(f"{width_value}x{height_value}")

root.title("Window Resizer")

#Heading
Label(root,text= "Window Resizer", font= "comicsansms 13 bold",padx= 20, pady= 10).grid(row= 0, column= 2)

width= Label(root, text= "Width").grid(row=1, column=1)
height= Label(root, text= "Height").grid(row=2, column=1)


width = StringVar()
height = StringVar()


widthentry = Entry(root, textvariable= width).grid(row= 1, column= 2)
heightentry = Entry(root, textvariable= height).grid(row= 2, column= 2)


Button(text = "Apply", command=resize , font= "comicsansms 13 bold", pady=2 ).grid( row=3,column=2)


root.mainloop()


