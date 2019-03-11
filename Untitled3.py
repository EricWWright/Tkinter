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
              text = "Choose your favorite movie"
              ).grid(sticky=W)
        # create instruction label
        Label(self,
              text = "Select all that apply:"
              ).grid(sticky=W)

        # create checkboxes
        # self.likes_comedy = BooleanVar()
        # Checkbutton(self,
        #             text = "Comedy",
        #             variable = self.likes_comedy,
        #             command = self.update_text
        #             ).grid(sticky=W)
        # self.likes_drama = BooleanVar()
        # Checkbutton(self,
        #             text="Drama",
        #             variable=self.likes_drama,
        #             command=self.update_text
        #             ).grid(sticky=W)
        # self.likes_romance = BooleanVar()
        # Checkbutton(self,
        #             text="Romance",
        #             variable=self.likes_romance,
        #             command=self.update_text
        #             ).grid(sticky=W)

        # create radiobuttons
        self.favorite = StringVar()
        self.favorite.set(None)

        Radiobutton(self,
                    text="Comedy",
                    variable=self.favorite,
                    value = "comedy.",
                    command=self.update_text
                    ).grid(sticky=W)
        
        Radiobutton(self,
                    text="Drama",
                    variable=self.favorite,
                    value = "drama.",
                    command=self.update_text
                    ).grid(sticky=W)
        
        Radiobutton(self,
                    text="Romance",
                    variable=self.favorite,
                    value = "romance.",
                    command=self.update_text
                    ).grid(sticky=W)

        # create text widget to display message
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
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

        message = "Your favorite type of movie is "
        message += self.favorite.get()

        self.results_txt.delete(0.0,END)
        self.results_txt.insert(0.0,message) 

# main
root = Tk()
root.title("Movie Chooser")
app = Application(root)
root.mainloop()
