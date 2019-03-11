from tkinter import *

class Application(Frame):
    """ GUI application which can reveal the secret of longevity. """

    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        # create instruction label
        self.inst_lbl = Label(self, text = "Enter password for the secret of life")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        # create label for password
        self.pw_lbl = Label(self, text = "Password: ")
        self.pw_lbl.grid(row = 1, column = 0, sticky = E)
        # create entry widget to accept password
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)
        # create submit button
        self.submit_bttn = Button(self, text = "Submit", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = NSEW)
        # create text widget to display message
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = NSEW)
    
    def reveal(self):
        password = self.pw_ent.get()
        if password == "secret":
            message = "Here's the secret of life............42"
        else:
            message = "That's not the correct password, so I can't share the secret with you."
        self.secret_txt.delete(0.0, END) # row.character, END
        self.secret_txt.insert(0.0, message)

    
# main
root = Tk()
root.title("Secret of life")
root.geometry("300x150")

app = Application(root)

root.mainloop()
