#!/usr/bin/python3

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master) #tkinter
        self.master = master #tkinter
        self.pack() #tkinter
        self.create_widgets() #pseudo

    def create_widgets(self):
        self.hi_there = tk.Button(self) #Hello world Button defenition
        self.hi_there["text"] = "Hello World\n(click me)" #
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top") # Roughly saying, put Button!

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy) # Method to end applicaion!
        self.quit.pack(side="bottom") #Roughly saying, put Button!


    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

