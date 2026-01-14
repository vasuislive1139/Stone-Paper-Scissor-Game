import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("🎮 Rock Paper Scissors ✂️")
root.geometry("520x550")
root.config(bg="#a6dcef")

player_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissors"]

gradient_frame = tk.Canvas(root, width=520, height=550, highlightthickness=0)
gradient_frame.pack(fill="both", expand=True)
for i in range(256):
    color = f"#{int(166 - i/2):02x}{int(220 - i/4):02x}{int(239 - i/8):02x}"
    gradient_frame.create_line(0, i*2, 520, i*2, fill=color)

ui_frame = tk.Frame(root, bg="#a6dcef", highlightthickness=0)
ui_frame.place(relx=0.5, rely=0.5, anchor="center")

def play(player_choice):
    global player_score, computer_score
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        outcome = "🤝 It's a Draw!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        player_score += 1
        outcome = "🎉 You Win!"
    else:
        computer_score += 1
        outcome = "💻 Computer Wins!"

    result_label.config(
        text=f"{outcome}\nYou chose {player_choice}, Computer chose {computer_choice}",
        fg="#1f1f1f"
    )
    update_scoreboard()
    check_winner()

def update_scoreboard():
    player_label.config(text=f"👤 Player: {player_score}")
    computer_label.config(text=f"💻 Computer: {computer_score}")

def check_winner():
    global player_score, computer_score
    if player_score == 5 or computer_score == 5:
        winner = "🏆 Congratulations you Won!" if player_score > computer_score else "💻 Computer Wins the Game!"
        messagebox.showinfo("Game Over", winner)
        reset_game()

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    result_label.config(text="Make your move!", fg="red")
    update_scoreboard()

def on_enter(e):
    e.widget.config(bg="#7bed9f")

def on_leave(e):
    e.widget.config(bg="white")

title = tk.Label(ui_frame, text="🪨 Rock Paper Scissors ✂️", font=("Poppins", 22, "bold"), bg="#a6dcef", fg="#2f3542")
title.pack(pady=20)

result_label = tk.Label(ui_frame, text="Make your move!", font=("Arial", 14, "bold"), bg="#a6dcef", fg="red")
result_label.pack(pady=10)

btn_frame = tk.Frame(ui_frame, bg="#a6dcef")
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, text="🪨 Rock", font=("Arial", 16, "bold"),
                     bg="white", width=10, height=2, command=lambda: play("Rock"))
paper_btn = tk.Button(btn_frame, text="✋ Paper", font=("Arial", 16, "bold"),
                      bg="white", width=10, height=2, command=lambda: play("Paper"))
scissors_btn = tk.Button(btn_frame, text="✂️ Scissors", font=("Arial", 16, "bold"),
                         bg="white", width=10, height=2, command=lambda: play("Scissors"))

for btn in (rock_btn, paper_btn, scissors_btn):
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)

score_frame = tk.Frame(ui_frame, bg="#1abc9c", bd=3, relief="ridge")
score_frame.pack(pady=20)

player_label = tk.Label(score_frame, text="👤 Player: 0", font=("Arial", 14, "bold"), bg="#1abc9c", fg="white")
player_label.grid(row=0, column=0, padx=30)
computer_label = tk.Label(score_frame, text="💻 Computer: 0", font=("Arial", 14, "bold"), bg="#1abc9c", fg="white")
computer_label.grid(row=0, column=1, padx=30)

reset_btn = tk.Button(ui_frame, text="🔁 Reset", font=("Arial", 13, "bold"), bg="red", fg="white", width=10, command=reset_game)
reset_btn.pack(pady=20)

root.mainloop()
