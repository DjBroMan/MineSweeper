import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Styled Disabled Button")

# Create a Style object
style = ttk.Style()
style.configure("TButton", font=("Arial", 12))
style.map("TButton", 
          foreground=[("disabled", "darkgray")], 
          background=[("disabled", "lightgray")])

# Function to disable the button
def disable_button():
    button.config(state=tk.DISABLED)

# Create a Button widget using ttk
button = ttk.Button(root, text="Click Me", command=disable_button)
button.pack(pady=20)

# Disable button on click
disable_button_btn = ttk.Button(root, text="Disable Button", command=disable_button)
disable_button_btn.pack()

# Run the application
root.mainloop()
