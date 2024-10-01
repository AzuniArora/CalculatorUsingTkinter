import tkinter as tk
from datetime import date

def calculate_age():
    birth_date = date(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    result_label.config(text=f"Your age is {age}")

# Create the main window
window=tk.Tk()
window.title("Calculation Tool")
window.geometry("900x500")
window.config(bg="#fe4d57")


# heading

tk.Label(window,text="Age Calculator",font="times 30 underline",bg="#fe4d57").pack()

# Create the input fields
day_label = tk.Label(window, text="Day:",bg="#fe4d57", font="arial 20")
day_label.place(x=150,y=80)
day_entry = tk.Entry(window, width=30, font="arial 20")
day_entry.place(x=250,y=80)

month_label = tk.Label(window, text="Month:",bg="#fe4d57", font="arial 20")
month_label.place(x=150,y=140)
month_entry = tk.Entry(window,width=30, font="arial 20")
month_entry.place(x=250,y=140)

year_label = tk.Label(window, text="Year:",bg="#fe4d57", font="arial 20")
year_label.place(x=150,y=200)
year_entry = tk.Entry(window,width=30, font="arial 20")
year_entry.place(x=250,y=200)

# Create the calculate button
calculate_button = tk.Button(window,bg="#fecd53",font="arial 20", text="Calculate Age", command=calculate_age)
calculate_button.place(x=300,y=250)

# Create the result label
result_label = tk.Label(window, text="",bg="#fe4d57",font="arial 20")
result_label.place(x=350,y=350)

# Start the Tkinter event loop
window.mainloop()
