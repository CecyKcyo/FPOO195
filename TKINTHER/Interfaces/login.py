import tkinter as tk

# Function to create the login interface
def create_login_interface():
    # Create a new Tkinter window
    window = tk.Tk()

    # Set the window title
    window.title("MERKS AND SPEN")

    # Set the window size
    window.geometry("400x200")

    # Create a frame for the logo
    logo_frame = tk.Frame(window)
    logo_frame.pack(side=tk.TOP, pady=10)

    # Add a label for the logo
    logo_label = tk.Label(logo_frame, text="MERKS AND SPEN", font=("Arial", 16))
    logo_label.pack()

    # Create a frame for the form
    form_frame = tk.Frame(window)
    form_frame.pack(side=tk.TOP, pady=10)

    # Add a label and entry for the email
    email_label = tk.Label(form_frame, text="Correo:", font=("Arial", 12))
    email_label.grid(row=0, column=0, sticky=tk.W, pady=2)
    email_entry = tk.Entry(form_frame, width=30)
    email_entry.grid(row=0, column=1, pady=2)

    # Add a label and entry for the password
    password_label = tk.Label(form_frame, text="Contraseña:", font=("Arial", 12))
    password_label.grid(row=1, column=0, sticky=tk.W, pady=2)
    password_entry = tk.Entry(form_frame, width=30, show="*")
    password_entry.grid(row=1, column=1, pady=2)

    # Add a login button
    login_button = tk.Button(window, text="INICIAR SESIÓN", bg="grey", font=("Arial", 12))
    login_button.pack(side=tk.TOP, pady=10)

    # Run the Tkinter event loop
    window.mainloop()

# Call the function to create the login interface
create_login_interface()
