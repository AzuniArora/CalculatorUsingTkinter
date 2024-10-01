from tkinter import *
from PIL import Image,ImageTk
import os

def f1():
    root.withdraw()
    os.system("python screen2.py")
    root.deiconify()
root=Tk()
root.geometry('800x500')
#root.configure(bg="white")
root.title("imagetool")

#original_img = Image.open("pic1.png")
original_img = Image.open("pic4.jpg")
resized_image1 = original_img.resize((1000, 500))
photo1 = ImageTk.PhotoImage(resized_image1)



Label(root,image=photo1).place(x=-10,y=0)

Label(root, text="Mathematical \n calculator",bg="#fe4d57", fg="white", font="poppin 35 underline").place(x=460,y=100)
Button(root,text="Let's Start",bg="#fecc4f",font="helavectia 20", padx=20, command=f1).place(x=500,y=300)

root.mainloop()


