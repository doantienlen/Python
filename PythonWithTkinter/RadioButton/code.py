from tkinter import * 

root = Tk()
root.geometry("200x200")
root.title("Listen Radio")

#  tkinter string variable able to store any string value 
v = StringVar(root, "1")

#  Dictionary to create multiple buttons 
values = { "Radio one": " 1",
            "Radio two": " 2",
            "Radio three": " 3",
            "Radio four": " 4",
            "Radio five": " 5",}
# loop is used to create multiple radio
# rather than creating each button separately 
for (text, value) in values.items(): 
    Radiobutton(root, text= text, variable= v, 
                value= value, indicator= 0, 
                background= "light blue").pack(fill=X, ipady=5)
mainloop()
