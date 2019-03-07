from tkinter import *

class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        """ Create three buttons that do nothing. """
        # create first button
        self.button1 = Button(self, text="button 1")
        self.button1.grid()
        self.label = Label(self, text="this is a button")
        self.label.grid()

        # create second button
        self.button2 = Button(self, text="button 2")
        self.button2.grid()
        self.label2 = Label(self, text="This is another button")
        self.label2.grid()

        # create third button
        self.button3 = Button(self)
        self.button3["text"] = "button 3"
        self.button3["bg"] = "green"
        self.button3["fg"] = "black"
        self.button3.grid()

root = Tk()
root.title("Lazy Buttons 2")
root.geometry("200x150")
app = Application(root)
root.mainloop()
