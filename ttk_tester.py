

from tkinter import *
import tkinter.ttk as ttk
import tkinter.scrolledtext
from datetime import datetime, date, time


def main(argv=None):
    if argv is None:
        argv = sys.argv
    gui = GuiClass()
    gui.go()
    return 0

class GuiClass(object):
    def __init__(self):

        self.root = Tk()
        self.root.title("Python tkinter example")

        self.testString = StringVar(value="Label 4")

        # Top Left Frame
        self.Frame1 = ttk.Frame(self.root,borderwidth=5, relief="sunken")
        self.Frame1.grid(column = 0, row = 0)

        self.Button1 = ttk.Button(self.Frame1,text="Button 1",command=lambda arg = 1: self.buttonPress(arg))
        self.Button1.grid(column = 0, row = 2)

        Label1 = ttk.Label(self.Frame1, text="Label 1")
        Label1.grid(column = 0, row = 0)

    
        # Top Middle Frame
        self.Frame2 = ttk.Frame(self.root,borderwidth=5, relief="sunken")
        self.Frame2.grid(column = 1, row = 0)

        Label2 = ttk.Label(self.Frame2, text="Label 2")
        Label2.grid(column = 0, row = 0)

        self.Button2 = ttk.Button(self.Frame2,text="Button 2",command=lambda arg = 2: self.buttonPress(arg))
        self.Button2.grid(column = 0, row = 1)
        

        # Top Right Frame
        self.Frame3 = ttk.Frame(self.root,borderwidth=5, relief="sunken")
        self.Frame3.grid(column = 2, row = 0)

        Label3 = ttk.Label(self.Frame3, text="Label 3")
        Label3.grid(column = 0, row = 0)

        self.Button3 = ttk.Button(self.Frame3,text="Button 3",command=lambda arg = 3: self.buttonPress(arg))
        self.Button3.grid(column = 0, row = 2)
        

        # Middle Left Frame

        self.startTimeVar = IntVar()      
        self.endTimeVar = IntVar(value=360)  
        
        self.Frame4 = ttk.Frame(self.root,borderwidth=5, relief="sunken")
        self.Frame4.grid(column = 0, row = 1, columnspan = 1, sticky = (E,W))

        self.startTimeScale = Scale(self.Frame4, orient=HORIZONTAL, length=100, resolution = 5, \
                                  from_=0, to=360, variable = self.startTimeVar)
        self.startTimeScale.grid(row=0,column=0)
        self.startTimeScale.set(0)
        
        startTimeEntry = ttk.Entry(self.Frame4, width=6,textvariable = self.startTimeVar)
        startTimeEntry.grid(column = 0, row = 1)
        

        # Middle text Frame
        self.Frame5 = ttk.Frame(self.root,borderwidth=5, relief="sunken")
        self.Frame5.grid(column = 1, row = 1, columnspan = 2)

        self.TextBox = tkinter.scrolledtext.ScrolledText(self.Frame5,height=8,width= 25)
        self.TextBox.grid(column = 0, row = 0)
        self.TextBox.insert('1.0', 'A text box')
        

        # Bottom Row
        self.Frame6 = ttk.Frame(self.root,borderwidth=5, relief="sunken")
        self.Frame6.grid(column = 0, row = 2, columnspan = 3)

        self.timeLabel = StringVar()
        Label5 = ttk.Label(self.Frame6, textvariable = self.timeLabel)
        Label5.grid(column = 0, row = 0)

    def buttonPress(self, num):
        time = datetime.now()
        tempStr = str(num)+" at "+str(time.strftime("%H:%M:%S")+"\n")
        self.TextBox.insert('1.0', tempStr)
        return       

    def periodic_check(self):
        # http://docs.python.org/dev/library/datetime.html#strftime-strptime-behavior
        time = datetime.now()
        self.timeLabel.set(time.strftime("%B %d ---- %H:%M:%S"))        
        self.root.after(100, self.periodic_check)

    def go(self):
        self.root.after(100, self.periodic_check)
        self.root.mainloop()


if __name__ == "__main__":
    sys.exit(main())  
