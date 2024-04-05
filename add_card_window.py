import customtkinter as ctk

class AddCardWindow(ctk.CTk):
    def __init__(self, main_app, add_card_callback):
        super().__init__()
        self.title("Add Card")
        self.geometry("300x300")

        self.main_app = main_app  # Reference to the main CardManager app
        self.add_card_callback = add_card_callback  # Function to add/edit cards in main app
        self.edit_card = None  # Stores the card being edited (if any)

        self.create_widgets()

    def create_widgets(self):
        # Create labels and entry fields for account, username, password, and email
        self.account_label = ctk.CTkLabel(self, text="Account:")
        self.account_label.pack()

        self.account_entry = ctk.CTkEntry(self)
        self.account_entry.pack()

        self.username_label = ctk.CTkLabel(self, text="Username:")
        self.username_label.pack()

        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.pack()

        self.password_label = ctk.CTkLabel(self, text="Password:")
        self.password_label.pack()

        self.password_entry = ctk.CTkEntry(self, show="*")  # Password hidden by default
        self.password_entry.pack()

        self.email_label = ctk.CTkLabel(self, text="Email:")
        self.email_label.pack()

        self.email_entry = ctk.CTkEntry(self)
        self.email_entry.pack()

        # Create buttons for saving/canceling and potentially editing (if applicable)
        if self.edit_card:  # Editing an existing card
            self.save_button = ctk.CTkButton(self, text="Save Changes", command=self.save_card)
        else:
            self.save_button = ctk.CTkButton(self, text="Add Card", command=self.save_card)
        self.save_button.pack()

        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.close_window)
        self.cancel_button.pack()

    def set_edit_card(self, card):
        # Populate UI elements with data from the card being edited
        self.edit_card = card
        self.account_entry.insert(0, card.account)
        self.username_entry.insert(0, card.username)
        self.password_entry.insert(0, card.password)  # Consider secure password handling during editing
        self.email_entry.insert(0, card.email)

    def save_card(self):
        account = self.account_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        # Call the add_card function from the main app, passing edit_card if applicable
        self.add_card_callback(account, username, password, email, self.edit_card)

    def close_window(self):
        self.withdraw()  # Hide the add card window
