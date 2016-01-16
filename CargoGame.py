from Tkinter import*
import tkMessageBox

def doo():
    launch = Tk()
    w=OptionMenu(launch,"1","1","2","3")
    w.pack()
    if w == 1:
        t=Text(launch, height=2 )
        t.pack()
        t.insert(END, "Hello")
    else:
        exit

    
root =Tk()


menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="Launch",menu=subMenu )
subMenu.add_command(label="New Project", command=doo)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doo)


#*****toolbar*****



root.mainloop()
