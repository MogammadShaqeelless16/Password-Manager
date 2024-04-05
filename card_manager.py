import customtkinter as ctk
from my_card_widget import MyCardWidget
from password_card import PasswordCard
from add_card_window import AddCardWindow
import json

class CardManager(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.geometry("600x400")

        self.cards = self.load_cards_from_json()  # Load existing cards from JSON
        self.create_widgets()

    def create_widgets(self):
        # Create main layout frames
        self.dashboard_frame = ctk.CTkFrame(self)
        self.dashboard_frame.pack(fill=ctk.BOTH, expand=True)

        self.card_list_frame = ctk.CTkFrame(self.dashboard_frame)
        self.card_list_frame.pack(fill=ctk.BOTH, expand=True)

        self.add_card_button = ctk.CTkButton(
            self.dashboard_frame, text="Add Card", command=self.show_add_card_window
        )
        self.add_card_button.pack(side=ctk.BOTTOM, pady=10)

        # Create separate window for adding/editing cards (initially hidden)
        self.add_card_window = AddCardWindow(self, self.add_card)  # Pass add_card function as callback

        # Assuming you have a container for displaying cards (e.g., frame)
        self.card_container = ctk.CTkFrame(self.card_list_frame)
        self.card_container.pack(fill="both", expand=True)

        # Iterate through loaded cards and create UI elements for each card
        for card in self.cards:
            # Create a card widget (e.g., frame) with details from the card dictionary
            card_widget = MyCardWidget(self.card_container, card["account"], card["username"], card["password"], card["email"])
            card_widget.pack(side="left", padx=10, pady=10)  # Pack cards side by side

    def show_add_card_window(self):
        self.add_card_window.deiconify()  # Make add card window visible

    def add_card(self, account, username, password, email, edit_card=None):
        new_card = PasswordCard(self, account, username, password, email, self.handle_password_visibility)
        if edit_card:  # Editing an existing card
            self.cards.remove(edit_card)
            self.card_container.destroy()  # Clear existing card list
            self.create_widgets()  # Repopulate with updated cards
        else:
            self.cards.append(new_card)
        new_card.pack(side="left", padx=10, pady=10)  # Add card to dashboard
        self.save_cards_to_json(self.cards)  # Save updated cards to JSON
        self.add_card_window.withdraw()  # Hide add card window

    def handle_password_visibility(self, is_visible):
        # Handle potential actions based on password visibility (e.g., logging)
        print(f"Password is now {'visible' if is_visible else 'hidden'} in a card")

    def load_cards_from_json(self):
        try:
            with open("cards.json", "r") as file:
                return json.load(file)  # Load data if file exists
        except FileNotFoundError:
            # Create an empty JSON file if it doesn't exist
            print("No existing cards found. Creating a new empty JSON file.")
            with open("cards.json", "w") as file:
                json.dump([], file, indent=4)  # Create empty JSON file
            return []  # Return an empty list

    def save_cards_to_json(self, cards):
        card_dicts = [{"account": card.account, "username": card.username, "password": card.password, "email": card.email} for card in cards]  # Use list comprehension

        with open("cards.json", "w") as file:
            json.dump(card_dicts, file, indent=4)
        return
