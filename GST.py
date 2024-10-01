import tkinter as tk
from tkinter import messagebox

def calculate_gst():
    try:
        original_amount = float(original_amount_entry.get())
        gst_rate = float(gst_rate_entry.get()) / 100

        gst_amount = original_amount * gst_rate
        total_amount = original_amount + gst_amount

        gst_label.config(text=f"GST Amount: ${gst_amount:.2f}")
        total_label.config(text=f"Total Amount (incl. GST): ${total_amount:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Create the main window

window=tk.Tk()
window.title("Calculation Tool")
window.geometry("900x500")
window.config(bg="#fe4d57")


# heading

tk.Label(window,text="GST Calculator",font="times 30 underline",bg="#fe4d57").pack(pady=40)


# Create the original amount input
original_amount_label = tk.Label(window, text="Original Amount ($):",bg="#fe4d57", font="arial 20")
original_amount_label.place(x=60,y=100)
original_amount_entry = tk.Entry(window,width=30, font="arial 20")
original_amount_entry.place(x=350,y=100)

# Create the GST rate input
gst_rate_label = tk.Label(window, text="GST Rate (%):",bg="#fe4d57", font="arial 20")
gst_rate_label.place(x=60,y=160)
gst_rate_entry = tk.Entry(window,width=30, font="arial 20")
gst_rate_entry.place(x=350,y=160)

# Create the calculate button
calculate_button = tk.Button(window,bg="#fecd53",font="arial 20", text="Calculate", command=calculate_gst)
calculate_button.place(x=500,y=230)

# Create the GST amount label
gst_label = tk.Label(window, text="",bg="#fe4d57", font="arial 20")
gst_label.place(x=150,y=300)

# Create the total amount label
total_label = tk.Label(window, text="",bg="#fe4d57", font="arial 20")
total_label.place(x=150,y=350)

# Start the Tkinter event loop
window.mainloop()
