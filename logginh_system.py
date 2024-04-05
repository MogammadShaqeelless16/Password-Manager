import tkinter as tk
from customtkinter import *
from tkinter import messagebox
import re

# Create users.txt file if it doesn't exist
try:
    with open("users.txt", "x"):
        pass
except FileExistsError:
    pass


# Function to sign up a new user
def sign_up():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password are empty
    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password!")
        return

    # Check for special characters in username
    if not re.match("^[a-zA-Z0-9_]+$", username):
        messagebox.showerror("Error", "Username should only contain letters, numbers, or underscores!")
        return

    # Check if username already exists
    with open("users.txt", "r") as file:
        for line in file:
            if username in line:
                messagebox.showerror("Error", "Username already exists!")
                return

    # Add new user to text file
    with open("users.txt", "a") as file:
        file.write(f"{username} {password}\n")
    messagebox.showinfo("Success", "User signed up successfully!")


# Function to log in
def log_in():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password are empty
    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password!")
        return

    # Check if username and password match
    with open("users.txt", "r") as file:
        found = False
        for line in file:
            stored_username, stored_password = line.strip().split()
            if username == stored_username and password == stored_password:
                found = True
                break

        if found:
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password!")


# GUI Setup
root = CTk()
root.title("Login System")
root.geometry("500x500")

# Calculate center position
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 550
window_height = 550
x_position = int((screen_width / 2) - (window_width / 2))
y_position = int((screen_height / 2) - (window_height / 2))

MAIN_FONT = "Cambria"  # This is the type of Font
MAIN_FONT_SIZE = 18 # Main font size sets the size of the main font
SECONDARY_MAIN_FONT_SIZE = 32 # Secondary Main font size sets the size of the Secondary main font

# Set window position
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Login Page
login_frame = CTkFrame(master=root)
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

login_label = CTkLabel(login_frame, text="Login",width=350,height=200,font=(MAIN_FONT,SECONDARY_MAIN_FONT_SIZE))
login_label.grid(row=0, column=0, columnspan=2)

username_label = CTkLabel(login_frame, text="Username:",font=(MAIN_FONT,MAIN_FONT_SIZE))
username_label.grid(row=1, column=0,pady=20)
username_entry = CTkEntry(login_frame)
username_entry.grid(row=1, column=1)

password_label = CTkLabel(login_frame, text="Password:",font=(MAIN_FONT,MAIN_FONT_SIZE))
password_label.grid(row=2, column=0,pady=5)

password_entry = CTkEntry(login_frame, show="*")
password_entry.grid(row=2, column=1)

blank_Space = CTkLabel(login_frame, text="""


""")
blank_Space.grid(row=3, column=0,pady=5)

login_button = CTkButton(login_frame, text="Login", command=log_in,font=(MAIN_FONT,MAIN_FONT_SIZE),width=150,height=40)
login_button.grid(row=4, column=0, columnspan=2,pady=10)

signup_button = CTkButton(login_frame, text="Sign Up", command=sign_up,font=(MAIN_FONT,MAIN_FONT_SIZE),width=150,height=40)
signup_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()