# to add image on a tkinter
# the genaral syntax: photo = PhotoImage(file = "path_of_file")
from tkinter import * 
from tkinter.ttk import * 
root = Tk()
root.geometry("500x500")
# Adding widgets to the root window 
Label(root,text="Hello World", font=('Verdana', 15)).pack(side= TOP, pady = 10 )
photo = PhotoImage(file= r"D:/codepython/learn_python_for_beger/TKINTER/vuonglekhon.png")

# Resizeing image to fit on button 
photoimage = photo.subsample(3,3)

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
Button(root, text='Click Me!', image= photoimage, compound= LEFT).pack(side=TOP)
mainloop()


