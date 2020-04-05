#!/usr/bin/python3

import math
import tkinter as tk

class Application(tk.Frame): #tk.Frame seems to be "window" obj
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.color_pic = tk.Frame(self, bg="#000000", height="100px", width="100px")
        self.color_pic.pack(side="left")
        self.color_pic.grid_propagate(0)

        self.r_scale = tk.Scale(self, label="Red", command=self.upd_r)
        self.g_scale = tk.Scale(self, label="Green",command=self.upd_g)
        self.b_scale = tk.Scale(self, label="Blue", command=self.upd_b)

        self.r_scale.pack(side="right")
        self.g_scale.pack(side="right")
        self.b_scale.pack(side="right")

    def upd_r(self, val):
        self.update_color(red=self.value_pass(val))
    def upd_g(self, val):
        self.update_color(green=self.value_pass(val))
    def upd_b(self, val):
        self.update_color(blue=self.value_pass(val))

    def value_pass(self, val):
        val = hex(int(int(val) * 2.55))
        if (len(str(val))==3):
            val = "0" + str(val)[2:]
        else:
            val = str(val)[2:]
        return val

    def update_color(self, red=None, green=None, blue=None):
        fr = self.color_pic
        new_color = str(fr["bg"])
        if red:
            new_color = str(new_color)[0] + red + str(new_color)[3:]
        if green:
            new_color = str(new_color)[0:3]  + green + str(new_color)[5:]
        if blue:
            new_color = str(new_color)[0:5] + blue
        fr["bg"]=new_color
        print(new_color)
        return


root = tk.Tk()
app = Application(master=root)
app.mainloop()
