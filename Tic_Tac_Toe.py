import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        a, b, c = combo
        if buttons[a]['text'] == buttons[b]['text'] == buttons[c]['text'] != "":
            for i in combo:
                buttons[i].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[a]['text']} wins!")
            root.quit()

def button_click(index):
    if buttons[index]["text"] == "":
        player = current_player.get()
        buttons[index]["text"] = player
        buttons[index]["fg"] = "red" if player == "X" else "blue"
        check_winner()
        toggle_player()

def toggle_player():
    current_player.set("O" if current_player.get() == "X" else "X")
    label.config(text=f"Player {current_player.get()}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = tk.StringVar(value="X")

label = tk.Label(root, text=f"Player {current_player.get()}'s turn", font=("Arial", 16))
label.grid(row=3, column=0, columnspan=3)

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=('Arial', 40), width=5, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()