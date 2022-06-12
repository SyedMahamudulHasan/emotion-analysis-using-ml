from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import *



root = Tk()

root.geometry("700x500")

# title of the applications
root.title("Mental Health Analysis Using ML")

# defining the frame
frame = Frame(root, width=600, height=800)
frame.place(anchor='center', relx=0.5, rely=0.5)

# title
Label(root, text = 'Check Your Mental Helth', font =('Verdana', 35)).pack(side = TOP, pady = 10)

# image
img = ImageTk.PhotoImage(Image.open('mentalimage.webp'))
label = Label(frame, image=img)
label.pack()


# This will create style object
style = Style()

# This will be adding style, and
# naming that style variable as
# W.Tbutton (TButton is used for ttk.Button).
style.configure('W.TButton', font =('calibri', 20, 'bold',),foreground = 'blue')

# Style will be reflected only on
# this button because we are providing
# style only on this Button.
''' Button'''
btn = Button(root, text = 'Start!',
                            style = 'W.TButton',
                         command = root.destroy).pack(side=BOTTOM, pady=28)



root.mainloop()
