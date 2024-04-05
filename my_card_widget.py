import customtkinter as ctk

class MyCardWidget(ctk.CTkFrame):
    def __init__(self, master, account, username, password, email):
        super().__init__(master)

        self.account_label = ctk.CTkLabel(self, text=f"Account: {account}")
        self.account_label.pack()

        self.username_label = ctk.CTkLabel(self, text=f"Username: {username}")
        self.username_label.pack()

        self.email_label = ctk.CTkLabel(self, text=f"Email: {email}")
        self.email_label.pack()

        # Placeholder for secure password display and management (consider secure libraries)
        self.password_label = ctk.CTkLabel(
            self, text=f"Password: {password if not self.is_password_visible else '•••••••••'}")
        self.password_label.pack()

        self.show_password_button = ctk.CTkButton(
            self, text="Show Password", command=self.toggle_password_visibility)
        self.show_password_button.pack()

        # Variable to track password visibility (initially hidden)
        self.is_password_visible = False

        # Store the password for later use
        self.password = password

    def toggle_password_visibility(self):
        self.is_password_visible = not self.is_password_visible

        if self.is_password_visible:
            # Show the actual password
            self.password_label.configure(text=f"Password: {self.password}")
            self.show_password_button.configure(text="Hide Password")
        else:
            # Hide the password
            self.password_label.configure(text="Password: •••••••••")
            self.show_password_button.configure(text="Show Password")
