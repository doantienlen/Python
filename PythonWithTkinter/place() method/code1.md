```python
# place() method in Tkinter 
# Syntax: widget.place(relx = 0.5, rely = 0.5, anchor = CENTER)
# place() method can be used with grid() method as well as with pack() method 
from tkinter import * 
from tkinter.ttk import *

root = Tk()
root.geometry("200x200")

# button widget 
b1 = Button(root, text="Click me!")
b1.place(relx = 1, x= -2, y= 2, anchor= NE )

# label widget 
l = Label(root, text="I'm a Label")
l.place(anchor= NW)

# button widget 
b2 = Button(root, text="GFG")
b2.place(relx= 5, rely= 0.5, anchor= CENTER)

root.mainloop()
```
After running the code. 

![image](https://user-images.githubusercontent.com/84562630/164253421-c7d4a4c8-7a6a-4a40-abad-16d8e648de00.png)

