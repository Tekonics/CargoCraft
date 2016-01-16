from Tkinter import *

class classtest:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printb = Button(frame, text="Print Message", command=self.printmessage, )
        self.printb.pack(side=LEFT)

        self.quit = Button(frame, text="Quit", command=frame.quit )
        self.quit.pack(side=LEFT)

    def printmessage(self):
        print"Wow, this worked!"

        
root = Tk()

b = classtest(root)

root.mainloop()

