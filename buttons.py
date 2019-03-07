from tkinter import *

#create the root window
root = Tk()

root.title("buttons program")
root.geometry("1500x1500")
root.configure(bg="black")

mainframe = Frame(root)
mainframe.grid()
mainframe.configure(bg="red")

label = Label(mainframe, text="these are buttons")
label.grid()

button1 = Button(mainframe, text="button 1")
button1.grid()

button2 = Button(mainframe, text="button 2")
button2.configure(bg="green",fg="blue")
button2.grid()

button3 = Button(mainframe)
button3["text"] = "button 3"
button3["bg"] = "yellow"
button3["fg"] = "purple"
button3.grid()


#kick off the window's event-loop
root.mainloop()
