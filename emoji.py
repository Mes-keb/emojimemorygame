import tkinter as tk
import random

difficulty_levels = {
    "Easy": ["🐶", "😸", "🐭", "🐹"],
    "Medium": [
        "🐶", "😸", "🐭", "🐹",
        "🦊", "🐻", "🐼", "🐸"
    ], 
    "Hard": [
        "🐶", "😸", "🐭", "🐹",
        "🦊", "🐻", "🐼", "🐸"
        "🐵", "🦁", "🐯", "🐨"
    ]
}


class EmojiMemoryGame:

    def __init__(self, root):
        self.root = root
        self.root.tittle("🧠 Emoji Memory Match")
        self.root.geometry("600x650")

        self.difficulty = tk.StringVar(value="Easy")

        self.create_menu()

    def create_menu(self):

        tk.Label(
            self.root,
            text="🧠 Emoji Memory Match"
            font=("Ariel", 24)
        ).pack(pady=20)

        tk.Label(
            self.root,
            text="Choose Difficulty",
            font=("Ariel", 16)
        ).pack()

        for level in difficulty_levels:
            tk.Button(
                self.root,
                text=level,
                variable=self.difficulty,
                value=level,
                font=("Ariel", 14)
            ).pack()

        tk.Button(
            self.root,
            text="🚀 Start Game",
            font=("Ariel", 16),
            command=self.start_game
        ).pack(pady=20)


        def start_game(self):

            for widget in self.root.winfo_children():
                widget.destroy()

            self.moves = 0
            self.matches =0
            self.open_cards = []

            emojis = difficulty_levels[self.difficulty]