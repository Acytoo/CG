from tkinter import *

def run(m):
    print(m)



root = Tk()

Button(root, text = 'Touch', command = lambda m='gaga' : run(m)).pack()
