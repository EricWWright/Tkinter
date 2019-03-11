from tkinter import *


class Application(Frame):
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        # create instruction label
        Label(self,
              text="asdfasdfasdf"
              ).grid(column=0, row=0, columnspan=2, sticky=W)
        # create instruction labels and entry widgits
        Label(self,
              text="asdfasdfasdf:"
              ).grid(column=0, row=1, columnspan=1, sticky=W)
        
        self.ent1 = Entry(self).grid(column=1, row=1, columnspan=2, sticky=W)

        Label(self,
              text="asdfasdfasdf:"
              ).grid(column=0, row=2, columnspan=1, sticky=W)
        
        self.ent2 = Entry(self).grid(column=1, row=2, columnspan=2, sticky=W)

        Label(self,
              text="asdfasdfasdf:"
              ).grid(column=0, row=3, columnspan=1, sticky=W)
        
        self.ent3 = Entry(self).grid(column=1, row=3, columnspan=2, sticky=W)

        # Create label and checkboxes
        Label(self,
              text="asdfasdfasdf:"
              ).grid(column=0, row=4, columnspan=1, sticky=W)

        self.ch1 = BooleanVar()
        Checkbutton(self,
                    text = "asdf",
                    variable = self.ch1,
                    command = self.update_text
                    ).grid(column=1, row=4, columnspan=1, sticky=W)
        self.ch2 = BooleanVar()
        Checkbutton(self,
                    text="asdf",
                    variable=self.ch2,
                    command=self.update_text
                    ).grid(column=2, row=4, columnspan=1, sticky=W)
        self.ch3 = BooleanVar()
        Checkbutton(self,
                    text="asdf",
                    variable=self.ch3,
                    command=self.update_text
                    ).grid(column=3, row=4, columnspan=1, sticky=W)

        # create label and radiobuttons
        Label(self,
              text="asdfasdfasdf:"
              ).grid(column=0, row=5, columnspan=1, sticky=W)

        self.option = StringVar()
        self.option.set(None)

        Radiobutton(self,
                    text="Asdf1",
                    variable=self.option,
                    value="asdf1",
                    command=self.update_text
                    ).grid(column=1, row=5, columnspan=1, sticky=W)

        Radiobutton(self,
                    text="Asdf2",
                    variable=self.option,
                    value="asdf2",
                    command=self.update_text
                    ).grid(column=2, row=5, columnspan=1, sticky=W)

        Radiobutton(self,
                    text="Asdf3",
                    variable=self.option,
                    value="asdf3",
                    command=self.update_text
                    ).grid(column=3, row=5, columnspan=1, sticky=W)
        # create submit button
        self.submit_bttn = Button(self,
                                text="Click for story"
                                ).grid(column=0, row=6, columnspan=1, sticky=W)

        # create text widget to display message
        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(sticky=W)

    def update_text(self):
        """Update text widget and display user's favorite movie types."""
        # likes = ""
        # if self.likes_comedy.get():
        #     likes += "You like comedic movies.\n"
        # if self.likes_drama.get():
        #     likes += "You like dramatic movies.\n"
        # if self.likes_romance.get():
        #     likes += "You like romantic movies.\n"

        # message = "Your favorite type of movie is "
        # message += self.favorite.get()

        # self.results_txt.delete(0.0, END)
        # self.results_txt.insert(0.0, message)


# main
root = Tk()
root.title("Madlibs")
app = Application(root)
root.mainloop()
