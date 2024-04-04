import customtkinter as ctk

class MyCardWidget(ctk.CTkFrame):
    def __init__(self, master, name, password, link):
        super().__init__(master)

        self.name_label = ctk.CTkLabel(self, text=f"Name: {name}")
        self.name_label.pack()

        self.link_label = ctk.CTkLabel(self, text=f"Link: {link}")
        self.link_label.pack()

        # Placeholder for secure password display and management (consider secure libraries)
        self.password_label = ctk.CTkLabel(
            self, text="Password: ••••••••• (hidden)")  # Replace with secure display mechanism
        self.password_label.pack()

        self.show_password_button = ctk.CTkButton(
            self, text="Show Password", command=self.toggle_password_visibility)
        self.show_password_button.pack()

        # Variable to track password visibility (initially hidden)
        self.is_password_visible = False

    def toggle_password_visibility(self):
        if self.is_password_visible:
            # Replace with actual password retrieval from a secure storage mechanism
            self.password_label.configure(text=f"Password: ••••••••• (hidden)")
            self.show_password_button.configure(text="Show Password")
        else:
            # IMPORTANT: Replace this with a secure password retrieval and display method
            # (avoid storing passwords in plain text)
            self.password_label.configure(text=f"Password: (PLACEHOLDER FOR PASSWORD)")
            self.show_password_button.configure(text="Hide Password")
        self.is_password_visible = not self.is_password_visible
