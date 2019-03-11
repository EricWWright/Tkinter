from tkinter import *


class Application(Frame):
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # create text widget to display message
        self.results_txt = Text(self, width=20, height=5, wrap=WORD)
        self.results_txt.grid(sticky=W)
        # create number buttons, opperator buttons, enterbutton, and clearbutton


# main
root = Tk()
root.title("Movie Chooser")
app = Application(root)
root.mainloop()
