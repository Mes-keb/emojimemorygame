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

            emojis = difficulty_levels[self.difficulty.get()]

            self.cards = emojis * 2
            random.shuffle(self.cards)

            self.info = tk.Label(
                self.root,
                font=("Arial", 15)
            )
            self.info.pack()

            self.board = tk.Frame(self.root)
            self.board.pack(pady=20)

            self.buttons = []

            columns = 4

            for i, emoji in enumerate(self.cards):

                button = tk.Button(
                    self.board,
                    text="❓",
                    width=6,
                    height=3
                    font=("Ariel", 18),
                    command=lambda i=i:self.flip(i)
                )

                button.grid(
                    row=i//columns,
                    columns=i%columns,
                    padx=5,
                    pady=5
                )

                self.buttons.append(button)
            
            self.message = tk.Label(
                self.root,
                font=("Ariel", 14)
            )   
            self.message.pack()

            self.update_info


            def flip(self,index):

                if len(self.open_cards)==2:
                    return
                
                if self.buttons[index]["text"]!="❓":
                    return
                
                self.buttons[index]["text"]=self.cards[index]

                self.open_cards.append(index)

                if len(self.open_cards)==2:
                    self.moves+=1
                    self.root.after(800,self.check)


                    def check(self):

                        a,b=self.open_cards

                        if self.cards[a]==self.cards[b]:

                            self.buttons[a]["state"]="disabled"
                            self.buttons[b]["state"]="disabled"

                            self.matches+=1
                            self.message.config(text="🎊 Great Match!")

                        else:

                            self.buttons[a]["text"]="❓"
                            self.buttons[b]["text"]="❓"

                            self.message.config(text="❌ Try Again")

                        self.open cards=[]

                        self.update_info()

                       if self.matches==len(self.cards)//2:

                            self.message.config(
                                text=f"🏆 You Win! Moves: {self.moves}"
                            ) 


                            def update_info(self):

                                self.info.config(
                                    text=f"Difficulty: {self.difficulty.get()}  | Moves: {self.moves}"
                                )


                                root=tk.TK()
                                game=EmojiMemoryGame(root)

                                root.mainloop()
                                