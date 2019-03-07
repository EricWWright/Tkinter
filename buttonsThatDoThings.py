from tkinter import *

class Application(Frame):
    """ GUI application which counts button clicks. """
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0 # number of button clicks
        self.create_widget()
    
    def create_widget(self):
        self.bttn1 = Button(self)
        self.bttn1["text"] = "Add Click"
        self.bttn1["command"] = self.add_count
        self.bttn1.grid()

        self.bttn2 = Button(self)
        self.bttn2["text"] = "Remove Click"
        self.bttn2["command"] = self.remove_count
        self.bttn2.grid()

        self.bttn3 = Button(self)
        self.bttn3["text"] = "Multiply Click"
        self.bttn3["command"] = self.multiply_count
        self.bttn3.grid()

        self.bttn4 = Button(self)
        self.bttn4["text"] = "Divide Click"
        self.bttn4["command"] = self.divide_count
        self.bttn4.grid()

        self.bttn5 = Button(self)
        self.bttn5["text"] = "Reset Clicks"
        self.bttn5["command"] = self.reset_count
        self.bttn5.grid()

        self.label = Label(self)
        self.label["text"] = "Total Clicks: 0"
        self.label.grid()

    def add_count(self):
        """ Increase click count and display new total. """
        self.bttn_clicks += 1
        self.label["text"] = "Total Clicks: " + str(self.bttn_clicks)
    
    def remove_count(self):
        """ Decrease click count and display new total. """
        if self.bttn_clicks == 0:
            self.label["text"] = "Total Clicks: 0"
        else:
            self.bttn_clicks -= 1
            self.label["text"] = "Total Clicks: " + str(self.bttn_clicks)
    
    def multiply_count(self):
        """ Multiplys click count by 2 and displays new total. """
        self.bttn_clicks = self.bttn_clicks * 2
        self.label["text"] = "Total Clicks: " + str(self.bttn_clicks)
    
    def divide_count(self):
        """ Divides click count by 2 and displays new total. """
        if self.bttn_clicks <= 0:
            self.bttn_clicks = 0
            self.label["text"] = "Total Clicks: 0"
        else:
            self.bttn_clicks = self.bttn_clicks / 2
            self.label["text"] = "Total Clicks: " + str(self.bttn_clicks)
    
    def reset_count(self):
        """ Resets the click count and displays new total. """
        self.bttn_clicks = 0
        self.label["text"] = "Total Clicks: 0"
    
root = Tk()
root.title("Click Counter")
root.geometry("300x150")
app = Application(root)
root.mainloop()
