from Tkinter import *


root = Tk()
x = 0
def a_1(event):
    if x == 0: 
        a = 1
        x = 1
        print a
    else:
        b = 1

def a_2(event):
    if x == 0: 
        a = 2
        x = 1
        print a
    else:
        b = 2

def a_3(event):
    if x == 0: 
        a = 3
        x = 1
        print a
    else:
        b = 3
def calc():
    y = a + b
    print y
topframe = Frame(root)
topframe.pack()

one = Button(root, text="One", bg="gray", fg="black")
one.bind("<Button-1>", a_1)
one.pack(side=LEFT)
two = Button(root, text="Two", bg="gray", fg="black")
two.bind("<Button-1>", a_2)
two.pack(side=LEFT)
three = Button(root, text="three", bg="gray", fg="black")
three.bind("<Button-1>", a_3)
three.pack(side=LEFT)
sub= Button(root, text="Calculate", bg="gray", fg="black")
sub.bind("<Button-1>", calc)
sub.pack(side=LEFT)

root.mainloop()

