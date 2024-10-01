import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())

        bmi = weight / (height ** 2)

        result_label.config(text=f"BMI: {bmi:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Create the main window
# Create the main window

window=tk.Tk()
window.title("Calculation Tool")
window.geometry("900x500")
window.config(bg="#fe4d57")


# heading

tk.Label(window,text="BMI Calculator",font="times 30 underline",bg="#fe4d57").pack(pady=40)



# Create the height input
height_label = tk.Label(window, text="Height (m):",bg="#fe4d57", font="arial 20")
height_label.place(x=60,y=100)
height_entry = tk.Entry(window,width=30, font="arial 20")
height_entry.place(x=350,y=100)

# Create the weight input
weight_label = tk.Label(window, text="Weight (kg):",bg="#fe4d57", font="arial 20")
weight_label.place(x=60,y=160)
weight_entry = tk.Entry(window,width=30, font="arial 20")
weight_entry.place(x=350,y=160)

# Create the calculate button
calculate_button = tk.Button(window,bg="#fecd53",font="arial 20", text="Calculate", command=calculate_bmi)
calculate_button.place(x=500,y=230)

# Create the result label
result_label = tk.Label(window, text="",bg="#fe4d57", font="arial 20")
result_label.place(x=150,y=300)

# Start the Tkinter event loop
window.mainloop()
