```python 
# place() method in Tkinter 
# Syntax: widget.place(relx = 0.5, rely = 0.5, anchor = CENTER)
# place() method can be used with grid() method as well as with pack() method 
from tkinter import * 
from tkinter.ttk import *

root = Tk()
root.geometry("200x200")

# button widget 
b2 = Button(root, text="GFG")
b2.pack(fill= X, expand= True, ipady= 10)

# button widget 
b1 = Button(root, text="Click me!")

# This is where b1 is placed inside b2 with in_ option 
b1.place(in_= b2, relx= 0.5, rely= 0.5, anchor= CENTER)

# label widget 
l = Label(root, text="I'm a Label")
l.place(anchor= NW)

root.mainloop()
```
After running the code: 

![image](https://user-images.githubusercontent.com/84562630/164255644-a238fa03-c6da-4d26-a9cc-e3dd95a5b33a.png)
