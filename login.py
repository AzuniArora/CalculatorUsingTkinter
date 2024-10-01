from tkinter import*
import sqlite3
from tkinter import messagebox


def login():
        import sqlite3
        con=sqlite3.connect('mydatabase.db')

        sql="select * from userregister"
        res=con.execute(sql)
        msg=False
        for row in res:
            print(row)
            if str(row[1])==str(em.get()) and str(row[2])== str(pw.get()):
                msg=True
        if msg:
            messagebox.showinfo('msg', "succ login")
            root.destroy()
            import screen5
            
        else:
            messagebox. showwarning('warning',"invalid details")
        em.set("")
        pw.set("")

        con.commit()
        con.close()
        
            
root=Tk()
root.title("Calculation Tool")
root.geometry("1000x500")
root.config(bg="#fe4d57")
em=StringVar()
pw=StringVar()


Label(root,text="Login",font="times 30 underline",bg="#fe4d57").pack()

Label(root,text="Email Id:",font="helavectia 20",bg="#fe4d57").place(x=150,y=80)
Entry(root,width=25,bd=2,font="helavectia 20",bg="white", textvariabl=em).place(x=400,y=80)

Label(root,text="Password:",font="helavectia 20",bg="#fe4d57").place(x=150,y=140)
Entry(root,width=25,bd=2,font="helavectia 20",bg="white",show="*", textvariable=pw).place(x=400,y=140)


Button(root,text="login",bg="#fecd53", fg="white",font="helavectia 20",bd=4,padx=7, command=login).place(x=500,y=320)
root.mainloop()
