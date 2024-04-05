import tkinter as tk
from tkinter import messagebox
# import customtkinter  as

def login():
    username = username_entry.get()
    password = password_entry.get()

    try:
        with open("user_credentials.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    messagebox.showinfo("Success", "Login Successful!")
                    return
            messagebox.showerror("Error", "Invalid username or password.")
    except FileNotFoundError:
        messagebox.showerror("Error", "User credentials file not found.")

def register():
    # Implement registration functionality here
    pass

root = tk.Tk()
root.title("Login")
root.geometry("500x500")

username_label = tk.Label(root, text="Username:")
username_label.pack(pady=(150, 5))

username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(root, text="Submit", command=login)
login_button.pack(pady=5)

register_button = tk.Button(root, text="Register", command=register)
register_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

# Center horizontally
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f"+{x}+{y}")

root.mainloop()
