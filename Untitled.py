from tkinter import *

root = Tk()
root.title("Labeler")
root.geometry("500x500")

# app = Frame(root)
# app.grid()


# lbl = Label(app, text = "I'm a label!", background = "black", fg= "red", font=("Helvetica", 275))
# lbl.grid()

C = Canvas(root, bg="black", height=500, width=500)

coord = 10, 50, 240, 210
pac = C.create_arc(coord, start=0, extent=300, fill="yellow")

dot = 10, 10, 10, 10
eat = C.create_arc(dot, start=200, extent=360, fill="white")


C.pack()

root.mainloop()
