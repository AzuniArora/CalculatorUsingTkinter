from tkinter import*
from PIL import Image,ImageTk


root=Tk()
root.geometry("800x500")
root.resizable(False,False)
def f1():
    root.destroy()
    import registerform
    
def f2():
    root.destroy()
    import login
    
#original_img = Image.open("pic1.png")
original_img = Image.open("photo/pic4.jpg")
resized_image1 = original_img.resize((1000, 500))
photo1 = ImageTk.PhotoImage(resized_image1)
Label(root,image=photo1).place(x=-10,y=0)





Label(root, text="Mathematical \n calculator",bg="#fe4d57", fg="white", font="poppin 35 underline").place(x=460,y=100)
Button(root,text="Register",bg="#fecc4f",font="helavectia 20", padx=20, command=f1).place(x=500,y=250)
Button(root,text="Login",bg="#fecc4f",font="helavectia 20", padx=40, command=f2).place(x=500,y=350)


root.configure(bg="#fafafa")
root.mainloop()
