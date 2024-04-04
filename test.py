import tkinter as tk
from tkinter import messagebox

class CustomEntry(tk.Frame):
    def __init__(self, master, label_text):
        super().__init__(master)
        
        self.label = tk.Label(self, text=label_text)
        self.label.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.entry = tk.Entry(self)
        self.entry.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.pack(pady=5)

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        
        self.geometry("500x500")
        
        self.username_entry = CustomEntry(self, "Username:")
        self.username_entry.pack(pady=(150, 5))  # Center vertically
        
        self.password_entry = CustomEntry(self, "Password:")
        self.password_entry.pack(pady=5)
        
        self.submit_button = tk.Button(self, text="Submit", command=self.login)
        self.submit_button.pack(pady=5)
        
        # Register button positioned at the bottom right
        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.register_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)
        
        # Center horizontally
        self.update_idletasks()  # Update geometry information
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"+{x}+{y}")
        
    def login(self):
        username = self.username_entry.entry.get()
        password = self.password_entry.entry.get()
        
        # Check login credentials (dummy implementation)
        if username == "admin" and password == "admin123":
            messagebox.showinfo("Success", "Login Successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password.")
    
    def register(self):
        # Implement registration functionality here
        messagebox.showinfo("Info", "Redirecting to registration page...")

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
