import tkinter as tk
from password_classes import Password 

if __name__ == "__main__":
    root=tk.Tk()
    password_generator = PasswordGenerador()
    app = ApplicationUI(root,password_generator)
    root.mainloop()
    