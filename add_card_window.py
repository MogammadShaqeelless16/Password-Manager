import customtkinter as ctk

class AddCardWindow(ctk.CTk):
    def __init__(self, main_app, add_card_callback):
        super().__init__()
        self.title("Add Card")
        self.geometry("300x250")

        self.main_app = main_app  # Reference to the main CardManager app
        self.add_card_callback = add_card_callback  # Function to add/edit cards in main app
        self.edit_card = None  # Stores the card being edited (if any)

        self.create_widgets()

    def create_widgets(self):
        # Create labels and entry fields for name, password, and link
        self.name_label = ctk.CTkLabel(self, text="Name:")
        self.name_label.pack()

        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.pack()

        self.password_label = ctk.CTkLabel(self, text="Password:")
        self.password_label.pack()

        self.password_entry = ctk.CTkEntry(self, show="*")  # Password hidden by default
        self.password_entry.pack()

        self.link_label = ctk.CTkLabel(self, text="Link:")
        self.link_label.pack()

        self.link_entry = ctk.CTkEntry(self)
        self.link_entry.pack()

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
        self.name_entry.insert(0, card.name)
        self.password_entry.insert(0, card.password)  # Consider secure password handling during editing
        self.link_entry.insert(0, card.link)

    def save_card(self):
        name = self.name_entry.get()
        password = self.password_entry.get()
        link = self.link_entry.get()

        # Call the add_card function from the main app, passing edit_card if applicable
        self.add_card_callback(name, password, link, self.edit_card)

    def close_window(self):
        self.withdraw()  # Hide the add card window
