import tkinter as tk

root = tk.Tk()
root.wm_geometry("200x200")
root.title("Authentication")
root.grid()

blue = tk.Canvas(height=100, width=115, background="Blue")
blue.grid(row= 0, column=0)

orange = tk.Canvas(height=100, width=115, background="Orange")
orange.grid(row= 1, column=0)

green = tk.Canvas(height=100, width=115, background="green")
green.grid(row= 0, column=1)

red = tk.Canvas(height=100, width=115, background="red")
red.grid(row= 1, column=1)

root.mainloop()