import tkinter as tk
from tkinter import messagebox

def save_credentials():
    user_name = username_entry.get()
    user_password = password_entry.get()
    
    if user_name and user_password:
        try:
            with open('user_credentials.txt', 'a') as file:
                file.write(f"{user_name},{user_password}\n")
            messagebox.showinfo("Success", "Credentials saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter both name and password.")

def login_forum():
    pass

# create main window
root = tk.Tk()
root.title("Registration")
root.geometry("500x500")

#create labels and inputs
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=(150, 5))

username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(root, text="Submit", command=save_credentials)
login_button.pack(pady=5)

register_button = tk.Button(root, text="Login", command=login_forum)
register_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

# Center horizontally
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f"+{x}+{y}")



root.mainloop()


