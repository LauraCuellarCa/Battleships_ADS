import tkinter as tk
player_name = ""

def create_welcome_window():
    root = tk.Tk()
    root.title("Welcome to Battleships Game")
    root.geometry("400x200")  # Set the window size
    root.configure(bg="white")  # Set the background color of the window

    # Welcome label
    welcome_label = tk.Label(root, text="Welcome to Battleships Game!", font=("Helvetica", 16, "bold"), fg="dark blue", bg="white")
    welcome_label.pack(pady=10)

    # Name entry
    name_var = tk.StringVar()
    name_label = tk.Label(root, text="Enter your name:", fg="dark blue", bg="white")
    name_label.pack()
    name_entry = tk.Entry(root, textvariable=name_var, bg="light grey", fg="dark blue")
    name_entry.pack(pady=10)

    # Button to start the game
    start_button = tk.Button(root, text="Start Game", command=lambda: get_player_name_start_game(name_var.get(), root), fg="dark blue", bg="white")
    start_button.pack()

    root.mainloop()

def get_player_name_start_game(playerName, root):
    global player_name
    # Do something with the player name (add to ranking list, etc.)
    player_name = playerName
    root.destroy()
