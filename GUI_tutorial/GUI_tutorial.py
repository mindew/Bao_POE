from PIL import Image, ImageTk
from tkinter import Tk, BOTH
from tkinter .ttk import Frame, Button, Style, Label
# Frame is a container for other widgets
# tutorial is from: http://zetcode.com/gui/tkinter/introduction/


class Example(Frame):

    def __init__(self):
        super().__init__()
        # class inherits from the frame container widget
        self.initUI()
        # delegate the creation of the user interface

    def initUI(self):

        Style().configure("TFrame", background="#333")
        # frame = dark gray background
        self.master.title("Absolute positioning")
        # set the title of the window
        # .master = gives access to the root window
        self.pack(fill=BOTH, expand=1)
        # pack() organizes widgets into horizontal
        # and vertical boxes.
        # Frame widget is accessed via the self attribute
        # to the Tk root window and expanded in both direction

        image1 = Image.open("plus.jpg")
        # create an image object
        image11 = ImageTk.PhotoImage(image1)
        # create a photo image object from an image
        label1 = Label(self, image=image11)
        # create a label with an image
        # labels can contain image / text
        label1.image = image11
        # reference to the image to prevent
        # image being garbage collected
        label1.place(x=20, y=20)
        # place the label

        image2 = Image.open("identicon.jpg")
        image22 = ImageTk.PhotoImage(image2)
        label2 = Label(self, image=image22)
        label2.image = image22
        label2.place(x=40, y=160)

        image3 = Image.open("facebook.jpg")
        image33 = ImageTk.PhotoImage(image3)
        label3 = Label(self, image=image33)
        label3.image = image33
        label3.place(x=170, y=50)

        # quitButton = Button(self, text="Quit", command=self.quit)
        # quitButton.place(x=50, y=50)

    def centerWindow(self):

        w = 290
        # width
        h = 150
        # height

        sw = self.master.winfo_screenwidth()
        # width of the screen
        sh = self.master.winfo_screenheight()
        # height of the screen

        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():

    root = Tk()
    # root window is created
    root.geometry("250x150+300+300")
    # sets a size for the window and positions it on the screen
    # width, height, x, y
    app = Example()
    # create the instance of the application class
    root.mainloop()
    # enters the mainloop
    # receives events from the window system and dispatches them
    # to the application widgets


if __name__ == '__main__':
    main()
