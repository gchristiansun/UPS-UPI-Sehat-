import tkinter as tk
from tkinter import messagebox
import globalVar

def popup():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    messagebox.showinfo("UPI Sehat", f"Selamat Datang {globalVar.list_data[0][1].strip()}!")
    root.after(3000, root.destroy)
