from tkinter import*
import sqlite3
from tkinter import messagebox
def show():
    
    root=Tk()
    root.geometry("1000x500")
    root.config(bg="#fe4d57")
    def sub():
        if pd.get()== cpd.get():
            if'@' in em.get() and '.' in em.get():


                con=sqlite3.connect('mydatabase.db')
                sql="create table if not exists userregister(name varchar(50),email varchar(50), password varchar(50))"
                con.execute(sql)


                sql="insert into userregister(name, email, password)values(?,?,?)"""
                data=(nm.get(), em.get(), pd.get())
                con.execute(sql,data)
                con.commit()
                con.close()
                messagebox.showinfo('msg', "succ register")
                nm.set("")
                em.set("")
                pd.set("")
                cpd.set("")
                root.destroy()
                import login
            else:
                messagebox.showwarning("warning","Invalid Email Id")
        else:
            messagebox.showwarning("warning","password and confirm password does n't match")
                
        
                
        
        
    nm=StringVar()    
    em=StringVar()
    pd=StringVar()
    cpd=StringVar()
        
    Label(root,text="User Register Form",font="Times 30 underline",bg="#fe4d57").pack()

    Label(root,text="Name:",font="helavectia 20",bg="#fe4d57").place(x=150,y=80)
    Entry(root,textvariable=nm,width=25,bd=2,font="helavectia 20",bg="white").place(x=400,y=80)

    Label(root,text="Email:",font="helavectia 20",bg="#fe4d57").place(x=150,y=140)
    Entry(root,textvariable=em,width=25,bd=2,font="helavectia 20",bg="white").place(x=400,y=140)

    Label(root,text="Password:",font="helavectia 20",bg="#fe4d57").place(x=150,y=200)
    Entry(root,textvariable=pd,width=25,bd=2,font="helavectia 20",bg="white", show="*").place(x=400,y=200)

    Label(root,text="Confirm Password:",font="helavectia 20",bg="#fe4d57").place(x=150,y=260)
    Entry(root,textvariable=cpd,width=25,bd=2,font="helavectia 20",bg="white",show="*").place(x=400,y=260)



    Button(root,text="Submit",bg="#fecc4f" ,font="helavectia 20",bd=4,padx=7,command=sub).place(x=500,y=320)
    root.mainloop()
show()

