import base64
from tkinter import *

def tiepAction(): 
    stringsYourCode.set("")
    stringsResult.set("")
def your_encode(): 
    s = str(stringsYourCode.get())
    b = s.encode("UTF-8")
    e = base64.b64encode(b)
    s1 = e.decode("UTF-8")
    stringsResult.set(s1)
def your_decode(): 
    s = str(stringsYourCode.get())
    if not str: 
        stringsResult.set("Invalid")
    else: 
        b = s.encode("UTF-8")
        e = base64.b64decode(b)
        s1 = e.decode("UTF-8")
        stringsResult.set(s1)
def main_screen(): 
    root = Tk()
    global stringsYourCode
    global stringsResult
    stringsYourCode= StringVar()
    stringsResult= StringVar()

    root.title("MY BASE64")
    root.minsize(height= 200, width=500)
    root.resizable(height= True, width= True)
    Label(root,text="Base64",fg="Blue",font=("tohama",16),justify=CENTER).grid(row= 0, columnspan=10)
    Label(root, text="Your code:").grid(row=1, column=0)
    Entry(root, width= 60, textvariable= stringsYourCode ).grid(row= 1, column=1 )

    frameButton= Frame(root)
    Button(frameButton, text="Encode", command= your_encode,activebackground="Red").pack(side= LEFT)
    Button(frameButton, text="Decode", command= your_decode,activebackground="Red").pack(side= LEFT)
    Button(frameButton, text="Continue", command= tiepAction, activebackground="Red").pack(side= LEFT)
    Button(frameButton, text="Exit", command= root.quit, activebackground="Red").pack(side= LEFT) 
    frameButton.grid(row=3, columnspan=2)

    Label(root, text="Result: ").grid(row=4, column=0)
    Entry(root, width=60, textvariable= stringsResult).grid(row=4, column=1)
    root.mainloop()
if __name__ == "__main__": 
    main_screen()