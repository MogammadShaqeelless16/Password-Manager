import customtkinter as ctk

class PasswordCard(ctk.CTkFrame):
    def __init__(self, master, account, username, password, email, show_password_callback):
        super().__init__(master)
        self.account = account
        self.username = username
        self.password = password
        self.email = email
        self.show_password_callback = show_password_callback
        self.show_password = False  # Initial state for password visibility

        self.create_widgets()

    def to_dict(self):
        return {
            "account": self.account,
            "username": self.username,
            "password": self.password,  # Consider secure password storage
            "email": self.email
        }

    def create_widgets(self):
        self.account_label = ctk.CTkLabel(self, text=f"Account: {self.account}")
        self.account_label.pack()

        self.username_label = ctk.CTkLabel(self, text=f"Username: {self.username}")
        self.username_label.pack()

        self.password_label = ctk.CTkLabel(
            self, text="Password: ••••••••• (hidden)")  # Replace with secure display mechanism
        self.password_label.pack()

        self.email_label = ctk.CTkLabel(self, text=f"Email: {self.email}")
        self.email_label.pack()

        self.show_password_button = ctk.CTkButton(
            self, text="Show" if not self.show_password else "Hide", command=self.toggle_password_visibility
        )
        self.show_password_button.pack()

    def toggle_password_visibility(self):
        self.show_password = not self.show_password
        self.password_label.config(show="*" if not self.show_password else "")
        if self.show_password_callback:  # Call a callback function if provided
            self.show_password_callback(self.show_password)  # Pass updated visibility state
