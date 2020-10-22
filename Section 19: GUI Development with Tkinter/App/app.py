import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello, {user_name.get() or 'World'}")

root = tk.Tk()
root.title("Hello")

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)

user_name = tk.StringVar()

name_label = ttk.Label(main, text="Name: ")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(main, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

greet_button = ttk.Button(main, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand=True)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="left", fill="x", expand=True)


root.mainloop()