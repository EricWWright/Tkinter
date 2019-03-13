from tkinter import *


class Application(Frame):
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.displayText = ""
        self.pos1 = ""
        self.pos2 = ""
        self.total = ""

    def create_widgets(self):
        # create text widget to display message
        self.display = Text(self, width=23, height=5, bg="black", fg="red", wrap=WORD)
        self.display.grid(column=0, row=0, columnspan=4)
        # create number buttons, opperator buttons, enterbutton, and clearbutton
        self.bttn7 = Button(self, 
                            text="7",
                            height=2,
                            width=5,
                            bg="black",
                            fg="red",
                            command=self.seven
                            )
        self.bttn7.grid(column=0, row=1)

        self.bttn8 = Button(self,
                            text="8",
                            height=2,
                            width=5,
                            bg="black",
                            fg="red",
                            command=self.eight
                            )
        self.bttn8.grid(column=1, row=1)

        self.bttn9 = Button(self,
                            text="9",
                            height=2,
                            width=5,
                            bg="black",
                            fg="red",
                            command=self.nine
                            )
        self.bttn9.grid(column=2, row=1)

        self.bttnDevide = Button(self,
                                 text="/",
                                 height=2,
                                 width=5,
                                 bg="black",
                                 fg="red",
                                 command=self.devide
                                 )
        self.bttnDevide.grid(column=3, row=1)

        self.bttn4 = Button(self,
                            text="4",
                            height=2,
                            width=5,
                            bg="black",
                            fg="red",
                            command=self.four
                            )
        self.bttn4.grid(column=0, row=2)

        self.bttn5 = Button(self,
                            text="5",
                            height=2,
                            width=5,
                            bg="black",
                            fg="red",
                            command=self.five
                            )
        self.bttn5.grid(column=1, row=2)

        self.bttn6 = Button(self,
                            text="6",
                            height=2,
                            width=5,
                            bg="black",
                            fg="red",
                            command=self.six
                            )
        self.bttn6.grid(column=2, row=2)

        self.bttnMultiply = Button(self,
                                   text="X",
                                   height=2,
                                   width=5,
                                   bg="black",
                                   fg="red",
                                   command=self.multiply
                                   )
        self.bttnMultiply.grid(column=3, row=2)

        self.bttn1 = Button(self,
                            text="1",
                            height=2,
                            width=5,
                            bg="black",
                            fg="red",
                            command=self.one
                            )
        self.bttn1.grid(column=0, row=3)

        self.bttn2 = Button(self,
                            text="2", 
                            height=2,
                            width=5,
                            bg="black",
                            fg="red",
                            command=self.two
                            )
        self.bttn2.grid(column=1, row=3)

        self.bttn3 = Button(self,
                            text="3",
                            height=2,
                            width=5,
                            bg="black",
                            fg="red",
                            command=self.three
                            )
        self.bttn3.grid(column=2, row=3)

        self.bttnMinus = Button(self,
                                text="-",
                                height=2,
                                width=5,
                                bg="black",
                                fg="red",
                                command=self.minus
                                )
        self.bttnMinus.grid(column=3, row=3)

        self.bttn0 = Button(self,
                            text="0",
                            height=2,
                            width=5,
                            bg="black",
                            fg="red",
                            command=self.zero
                            )
        self.bttn0.grid(column=1, row=4)

        self.bttnAdd = Button(self,
                              text="+",
                              height=2,
                              width=5,
                              bg="black",
                              fg="red",
                              command=self.add
                              )
        self.bttnAdd.grid(column=3, row=4)

        self.bttnClear = Button(self,
                                text="Clear",
                                height=2,
                                width=12,
                                bg="black",
                                fg="red",
                                command=self.clear
                                )
        self.bttnClear.grid(column=0, row=5, columnspan=2)

        self.bttnEquals = Button(self,
                                 text="=",
                                 height=2,
                                 width=12,
                                 bg="black",
                                 fg="red",
                                 command=self.equals
                                 )
        self.bttnEquals.grid(column=2, row=5, columnspan=2)
    
    def seven(self):
        self.displayText += "7"
        self.display.delete(0.0, END)
        self.display.insert(0.0, self.displayText)
    
    def eight(self):
        self.displayText += "8"
        self.display.delete(0.0, END)
        self.display.insert(0.0, self.displayText)
    
    def nine(self):
        self.displayText += "9"
        self.display.delete(0.0, END)
        self.display.insert(0.0, self.displayText)
    
    def four(self):
        self.displayText += "4"
        self.display.delete(0.0, END)
        self.display.insert(0.0, self.displayText)
    
    def five(self):
        self.displayText += "5"
        self.display.delete(0.0, END)
        self.display.insert(0.0, self.displayText)
    
    def six(self):
        self.displayText += "6"
        self.display.delete(0.0, END)
        self.display.insert(0.0, self.displayText)

    def one(self):
        self.displayText += "1"
        self.display.delete(0.0, END)
        self.display.insert(0.0, self.displayText)
    
    def two(self):
        self.displayText += "2"
        self.display.delete(0.0, END)
        self.display.insert(0.0, self.displayText)
    
    def three(self):
        self.displayText += "3"
        self.display.delete(0.0, END)
        self.display.insert(0.0, self.displayText)
    
    def zero(self):
        self.displayText += "0"
        self.display.delete(0.0, END)
        self.display.insert(0.0, self.displayText)
    
    def devide(self):
        self.displayText += "/"
        self.display.delete(0.0, END)
        self.display.insert(0.0, self.displayText)
    
    def multiply(self):
        self.displayText += "X"
        self.display.delete(0.0, END)
        self.display.insert(0.0, self.displayText)
    
    def minus(self):
        self.displayText += "-"
        self.display.delete(0.0, END)
        self.display.insert(0.0, self.displayText)
    
    def add(self):
        self.displayText += "+"
        self.display.delete(0.0, END)
        self.display.insert(0.0, self.displayText)
    
    def clear(self):
        self.displayText = ""
        self.display.delete(0.0, END)
        self.display.insert(0.0, self.displayText)

    def equals(self):
        self.displayText = self.total
        self.display.delete(0.0, END)
        self.display.insert(0.0, self.displayText)
    



# main
root = Tk()
root.title("Calculator")
root.configure(bg="black")
app = Application(root)
root.mainloop()
