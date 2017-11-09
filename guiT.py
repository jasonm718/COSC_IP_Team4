from Tkinter import *
from tkFileDialog import askopenfilename
import smoothen
import cv2
import numpy as np

filename = ""

class Application(Frame):

	

    def get_file(self):
    	self.filename = askopenfilename()
    	filename = self.filename
        self.url_label["text"] = self.filename

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Enter"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "right"})

        self.url_label = Label(self)
        self.url_label["text"] = "..."
        self.url_label.pack({"side": "right"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Image_Path"
        self.hi_there["command"] = self.get_file

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        root.geometry('{}x{}'.format(1000, 600))


root = Tk()
app = Application(master=root)
app.mainloop()

print(app.filename)
input_image = cv2.imread(app.filename, 0)
app = smoothen.smoothening((3,3), "gaussian", input_image)
blurred = app.smoothening()
mask = input_image - blurred

cv2.imwrite("blurred.jpg", blurred)
cv2.imwrite("mask.jpg", mask)
cv2.imwrite("sharpened.jpg", input_image - mask)

root.destroy()



