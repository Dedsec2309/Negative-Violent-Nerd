import tkinter
from tkinter import *
#import webbrowser
#import os
#Objects and Classes
def B1():
	Label(root,text="Hello World!").pack()


#Window
root = Tk()
root.title("Hello World!")
#Widgets
#Labels
Label(root,text="Hello World!").pack()
#Buttons
Button(root,text="Click Me!",command=B1).pack()
#Loop
root.mainloop()