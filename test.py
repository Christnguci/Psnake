import tkinter as tk
from tkinter import messagebox

# Create a Tkinter root window
root = tk.Tk()

# Hide the root window

# Show a pop-up message box with a message and an OK button
x=messagebox.askokcancel("Message", "This is a pop-up message box. Click OK to continue.")
print(x)
# Destroy the root window
root.destroy()