import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text = "enter the name") 
label.pack()

entry = tk.Entry(root)
entry.pack()

def show():
    print(entry.get())
button = tk.Button(root  ,text = "submit", command = show)
button.pack()

root.mainloop()
    

