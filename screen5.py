from tkinter import *
import os

def cal():
    root.withdraw()
    os.system("python calculator.py")
    root.deiconify()
def age():
    root.withdraw()
    os.system("python age.py")
    root.deiconify()
def per():
    root.withdraw()
    os.system("python percentage.py")
    root.deiconify()
def loan():
    root.withdraw()
    os.system("python loan.py")
    root.deiconify()
def pay():
    root.withdraw()
    os.system("python paypal.py")
    root.deiconify()

def st():
    root.withdraw()
    os.system("python salestax.py")
    root.deiconify()
def prob():
    root.withdraw()
    os.system("python probability.py")
    root.deiconify()
def bmi():
    root.withdraw()
    os.system("python bmi.py")
    root.deiconify()
def gst():
    root.withdraw()
    os.system("python GST.py")
    root.deiconify()

root=Tk()
root.geometry('850x550')
root.config(bg="#fe4d57")

Button(root,text="Simple Calculator",bg="#fecd53", font="helavectia 20",bd=4,padx=36, command=cal).place(x=100,y=50)
Button(root,text="Age Calculator",bg="#fecd53", font="helavectia 20",bd=4,padx=40, command=age).place(x=450,y=50)
Button(root,text="Percentage Calculator",bg="#fecd53", font="helavectia 20",bd=4,padx=7, command=per).place(x=100,y=150)
Button(root,text="Loan Calculator",bg="#fecd53", font="helavectia 20",bd=4,padx=38, command=loan).place(x=450,y=150)

Button(root,text="Paypal Calculator",bg="#fecd53", font="helavectia 20",bd=4,padx=33, command=pay).place(x=100,y=250)
Button(root,text="Sales Tax Calculator",bg="#fecd53", font="helavectia 20",bd=4,padx=7, command=st).place(x=450,y=250)
Button(root,text="Probability Calculator",bg="#fecd53", font="helavectia 20",bd=4,padx=10, command=prob).place(x=100,y=350)
Button(root,text="BMI Calculator",bg="#fecd53", font="helavectia 20",bd=4,padx=42, command=bmi).place(x=450,y=350)
Button(root,text="GST Calculator",bg="#fecd53", font="helavectia 20",bd=4,padx=20, command=gst).place(x=300,y=450)

    

root.mainloop()
