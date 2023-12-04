import tkinter as tk
from collections import deque
from Rankings import RankingSystem
import random
import subprocess
import sys
from cpu import CPU_Player


selected_direction = "U"  # Initial direction, you can change this as needed
game_state = 'placement'  # The initial state is 'placement'
userHitCount = 0
current_turn = "user"  # Can be 'user' or 'cpu'
player_name = ""

# Global variables for CPU strategy
cpu_hits = []  # List to store hit positions
section_shots = [[0 for _ in range(5)] for _ in range(5)]  # 5x5 sections for tracking shots
last_hit = None  # Track the last hit position for targeted shooting
target_mode = False  # Flag to indicate if CPU is in target mode (post-hit)
cpuHitCount = 0


cpu_player = CPU_Player()


game_ranking_system = RankingSystem()
game_ranking_system.add_player("A&DS")
game_ranking_system.add_player(player_name)
game_ranking_system.load_existing_players()


class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length


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
    global player_name, game_ranking_system
    # Do something with the player name (add to ranking list, etc.)
    player_name = playerName
    #game_ranking_system.add_player(player_name)
    root.destroy()


def create_grid(canvas, cell_size):
    line_width = 2
    line_color = "blue"

    # Create vertical and horizontal lines
    for i in range(11):
        canvas.create_line([(i * cell_size, cell_size), (i * cell_size, 11 * cell_size)], width=line_width,
                           fill=line_color)
        canvas.create_line([(0, i * cell_size), (11 * cell_size, i * cell_size)], width=line_width, fill=line_color)

    # Label columns (A-J) and rows (1-10)
    for i in range(10):
        canvas.create_text((i * cell_size + cell_size * 3 / 2, cell_size * 3 / 4), text=chr(65 + i), fill="red",
                           font=("Helvetica", 14))
        canvas.create_text((cell_size / 2, i * cell_size + cell_size * 5 / 4), text=str(i + 1), fill="red",
                           font=("Helvetica", 14))


def is_valid_placement(ship_length, start_row, start_col, direction, board):
    start_row -= 1
    start_col -= 1

    # Right direction
    if direction == "R":
        if start_col + ship_length > len(board):
            return False
        for i in range(ship_length):
            if board[start_row][start_col + i] != 0:
                return False

    # Left direction
    elif direction == "L":
        if start_col - ship_length + 1 < 0:  # Allow ship placement in the leftmost column
            return False
        for i in range(ship_length):
            if board[start_row][start_col - i] != 0:
                return False

    # Down direction
    elif direction == "D":
        if start_row + ship_length > len(board):
            return False
        for i in range(ship_length):
            if board[start_row + i][start_col] != 0:
                return False

    # Up direction
    elif direction == "U":
        if start_row - ship_length + 1 < 0:
            return False
        for i in range(ship_length):
            if board[start_row - i][start_col] != 0:
                return False

    return True




# Functions to inform the user that their ship placement was invalid
def show_temporary_label(text, duration):
    temp_label.config(text=text, fg="red", bg="yellow")
    temp_label.after(duration, clear_temporary_label)


def clear_temporary_label():
    temp_label.config(text="", bg="grey")


def draw_ship_on_canvas(canvas, ship_length, start_row, start_col, direction):
    ship_color = "gray"
    # Adjust start_row and start_col
    start_row += 1
    start_col += 1

    for i in range(ship_length):
        # Rest of your function...
        if direction == "R":
            canvas.create_rectangle((start_col + i) * cell_size, start_row * cell_size,
                                    (start_col + i + 1) * cell_size, (start_row + 1) * cell_size,
                                    fill=ship_color)

        elif direction == "L":
            canvas.create_rectangle((start_col - i) * cell_size, start_row * cell_size,
                                    (start_col - i + 1) * cell_size, (start_row + 1) * cell_size,
                                    fill=ship_color)

        elif direction == "D":
            canvas.create_rectangle(start_col * cell_size, (start_row + i) * cell_size,
                                    (start_col + 1) * cell_size, (start_row + i + 1) * cell_size,
                                    fill=ship_color)

        elif direction == "U":
            canvas.create_rectangle(start_col * cell_size, (start_row - i) * cell_size,
                                    (start_col + 1) * cell_size, (start_row - i + 1) * cell_size,
                                    fill=ship_color)


# Function to place CPU ships on the game board
def place_cpu_ships_on_board(enemy_game_board):
    ship_sizes = [5, 4, 3, 3, 2]
    if place_ships(enemy_game_board, ship_sizes, []):
        return enemy_game_board
    else:
        return None


def place_ships(grid, ships_to_place, placement_stack):
    if not ships_to_place:
        return True

    current_ship = ships_to_place[0]

    while True:
        orientation = random.choice(['horizontal', 'vertical'])
        x = random.randint(0, len(grid) - 1)
        y = random.randint(0, len(grid) - 1)

        if can_place_ship(grid, x, y, current_ship, orientation):
            place_ship(grid, x, y, current_ship, orientation)
            placement_stack.append((x, y, current_ship, orientation))

            if place_ships(grid, ships_to_place[1:], placement_stack):
                return True

            # Backtrack if we can't place the rest of the ships
            remove_ship(grid, *placement_stack.pop())

        if all_ships_placed(grid):
            break

    return False


def can_place_ship(grid, x, y, ship_size, orientation):
    grid_size = len(grid)

    if orientation == 'horizontal':
        if x + ship_size > grid_size:
            return False
        for i in range(ship_size):
            if grid[y][x + i] != 0:
                return False
    else:
        if y + ship_size > grid_size:
            return False
        for i in range(ship_size):
            if grid[y + i][x] != 0:
                return False

    return True


def place_ship(grid, x, y, ship_size, orientation):
    if orientation == 'horizontal':
        for i in range(ship_size):
            grid[y][x + i] = 1
    else:
        for i in range(ship_size):
            grid[y + i][x] = 1


def remove_ship(grid, x, y, ship_size, orientation):
    if orientation == 'horizontal':
        for i in range(ship_size):
            grid[y][x + i] = 0
    else:
        for i in range(ship_size):
            grid[y + i][x] = 0


def all_ships_placed(grid):
    for row in grid:
        if 0 in row:
            return False
    return True


def on_user_canvas_click(event):
    global current_ship, game_board, game_state, ship_queue
    if game_state != 'placement':
        return

    # Adjust for label row and column
    x = (event.x // cell_size) - 1
    y = (event.y // cell_size) - 1

    print(f"Clicked coordinates: ({x + 1}, {y + 1})")  # Adjusted for human-readable format (1-10 instead of 0-9)

    # Check if the click is within the grid (1-10) and if there is a ship to place
    if 0 <= x < 10 and 0 <= y < 10 and current_ship:
        # Rest of your function...
        # Check if the placement is valid
        if is_valid_placement(current_ship.length, y, x, selected_direction, game_board):
            # If valid, draw the ship on canvas and update the game board
            draw_ship_on_canvas(user_canvas, current_ship.length, y, x, selected_direction)
            for i in range(current_ship.length):
                if selected_direction == "R":
                    game_board[y][x + i] = 2
                elif selected_direction == "L":
                    game_board[y][x - i] = 2
                elif selected_direction == "D":
                    game_board[y + i][x] = 2
                elif selected_direction == "U":
                    game_board[y - i][x] = 2

            # Remove the placed ship from the queue and update the label
            ship_queue.popleft()
            if ship_queue:
                current_ship = ship_queue[0]
                shipLabel_text.set(f"Next ship to place: {current_ship.name} (length: {current_ship.length})")
            else:
                # No more ships to place, switch to battle mode
                game_state = 'battle'
                shipLabel_text.set("Battle mode: Click on the enemy grid to attack!")
                # Bind the click event to the enemy canvas for battle phase
                enemy_canvas.bind('<Button-1>', on_battle_click)
                # Unbind the ship placement function
                user_canvas.unbind('<Button-1>')
                dirLabel.destroy()
                dir_prompt_label.destroy()
                button_up.destroy()
                button_down.destroy()
                button_left.destroy()
                button_right.destroy()

        else:
            # If the placement is not valid, you can provide feedback to the user
            # text("Invalid placement. Try a different location or direction.")
            show_temporary_label("Invalid placement! Try a different location or direction.", 3000)


# Function to handle the click event in battle mode
def on_battle_click(event):
    global current_turn, enemy_game_board

    if game_state != 'battle' or current_turn != "user":
        return

    # Adjust for label row and column
    x = (event.x - cell_size) // cell_size
    y = (event.y - cell_size) // cell_size

    # Check if the click is within the grid (1-10)
    if 0 <= x < 10 and 0 <= y < 10:
        # Check if the cell has already been targeted
        if enemy_game_board[y][x] in [2, -1]:  # Assuming 2 is hit, -1 is miss
            show_temporary_label("Invalid try! Already targeted this cell.", 3000)
            return

        result = process_shot(y, x)
        display_hit_or_miss(enemy_canvas, x, y, result)  # Make sure to update the enemy canvas

        current_turn = "cpu"
        cpu_turn()


def cpu_turn():
    global current_turn, cpu_player, game_board, user_canvas
    if current_turn != "cpu":
        return

    row, col = cpu_player.choose_shot()
    result = process_cpu_shot(row, col)
    display_hit_or_miss(user_canvas, col, row, result)
    cpu_player.update_board(row, col, result)

    current_turn = "user"


def get_random_shot():
    # Find section with minimum shots
    min_shots = min(min(row) for row in section_shots)
    candidate_sections = []
    for i in range(5):
        for j in range(5):
            if section_shots[i][j] == min_shots:
                candidate_sections.append((i, j))

    selected_section = random.choice(candidate_sections)
    section_row, section_col = selected_section

    # Random shot within the selected section
    row = random.randint(section_row * 2, section_row * 2 + 1)
    col = random.randint(section_col * 2, section_col * 2 + 1)

    section_shots[section_row][section_col] += 1

    return row, col
# Function to process a shot at the given coordinates


def get_targeted_shot(last_hit):
    global game_board
    row, col = last_hit
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    random.shuffle(directions)  # Randomize directions to add unpredictability

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        # Check if the new cell is within the board
        if 0 <= new_row < 10 and 0 <= new_col < 10:
            # Then check if it's not already tried
            if game_board[new_row][new_col] == 0 or game_board[new_row][new_col] == 2:
                return new_row, new_col

    # If all adjacent cells have been tried, revert to random shot
    return get_random_shot()


def process_cpu_shot(row, col):
    global game_board
    if game_board[row][col] == 2:  # If a ship is present at the coordinates
        game_board[row][col] = 3  # Mark as hit by CPU
        return "Hit"
    elif game_board[row][col] == 0:  # If there is no ship at the coordinates
        game_board[row][col] = -1  # Mark as miss by CPU
        return "Miss"
    return "Already Tried"  # If the cell has already been guessed


def process_shot(row, col):
    # This function determines if a shot is a hit or a miss
    if enemy_game_board[row][col] == 1:  # If a ship is present at the guessed coordinates
        enemy_game_board[row][col] = 2  # Mark as hit
        return "Hit"
    elif enemy_game_board[row][col] == 0:  # If there is no ship at the guessed coordinates
        enemy_game_board[row][col] = -1  # Mark as miss
        return "Miss"
    return "Already Tried"  # If the cell has already been guessed


# Function to display hit or miss on the canvas
def display_hit_or_miss(canvas, col, row, result):
    global userHitCount, cpuHitCount
    # Adjust col and row
    col += 1
    row += 1
    center_x = (col + 0.5) * cell_size
    center_y = (row + 0.5) * cell_size
    if result == "Hit" and current_turn == "user":
        canvas.create_text(center_x, center_y, text="X", fill="red", font=("Helvetica", 14))
        userHitCount += 1
        if userHitCount == 17:
            enemy_canvas.unbind('<Button-1>')
            # Inform User they won
            youWon_label = tk.Label(root,
                                    text="Congratulations, Commander!\n Your strategic brilliance has sunk the enemy fleet!",
                                    font=("Helvetica", 25), bg="green")
            youWon_label.grid(row=0, column=0, columnspan=2,
                              pady=5)  # Adjust row, column, and other parameters as needed
            #Update Rankings
            game_ranking_system.record_play(player_name, won=True)
            game_ranking_system.record_play("A&DS", won=False)
            #Create View Rankings Button
            view_rankings_button = tk.Button(root, text="View Rankings", command=lambda: display_rankings(game_ranking_system))
            view_rankings_button.grid(row=6, column=0, columnspan=2, pady=5)


    elif result == "Hit" and current_turn == "cpu":
        canvas.create_text(center_x, center_y, text="X", fill="red", font=("Helvetica", 14))
        cpuHitCount += 1
        if cpuHitCount == 17:
            enemy_canvas.unbind('<Button-1>')
            # Inform User they won
            youWon_label = tk.Label(root,
                                    text="Sorry, Commander!\n You never stood a chance against Algorithms and Data Structures",
                                    font=("Helvetica", 25), bg="red")
            youWon_label.grid(row=0, column=0, columnspan=2,
                              pady=5)  # Adjust row, column, and other parameters as needed
            #Update Rankings
            game_ranking_system.record_play(player_name, won=False)
            game_ranking_system.record_play("A&DS", won=True)
            #Create View Rankings Button
            view_rankings_button = tk.Button(root, text="View Rankings", command=lambda: display_rankings(game_ranking_system))
            view_rankings_button.grid(row=6, column=0, columnspan=2, pady=5)



    elif result == "Miss":
        canvas.create_text(center_x, center_y, text="O", fill="blue", font=("Helvetica", 14))
    # You could also handle the "Already Tried" case if desired

def display_rankings(ranking_system):
    # Create a new Tkinter window
    window = tk.Tk()
    window.title("Player Rankings")
    window.geometry("500x450")  # Adjusted window size to accommodate the button
    window.config(bg="white")

    # Get ranking
    ranking = ranking_system.get_ranking()

    # Create title label
    title_label = tk.Label(window, text="Battleship Player Rankings", font=("Helvetica", 22, "bold"), bg="white", fg="dark blue")
    title_label.pack(pady=10)

    # Create labels to display player information
    for i, (player, stats) in enumerate(ranking):
        label_text = f"{i+1}. {player}: \t Plays - {stats['plays']}, Wins - {stats['wins']}"
        label = tk.Label(window, text=label_text, font=("Helvetica", 20), bg="white", fg="dark blue")
        label.pack()

    # Create "Play Again" button
    play_again_button = tk.Button(window, text="Play Again", command= restart_game, font=("Helvetica", 16), bg="dark blue", fg="white")
    play_again_button.pack(pady=20)

    # Run the Tkinter event loop
    window.mainloop()

def restart_game():
    game_ranking_system.save_data()
    subprocess.run([sys.executable, 'finaltest.py'])

#Start game with welcome window
create_welcome_window()

print(f"hi: {player_name}")

# Initialize the main Tkinter window
root = tk.Tk()
root.title('Battleship Game')

cell_size = 50

# Create canvases for the game
enemy_canvas = tk.Canvas(root, height=(cell_size * 11), width=(cell_size * 11), bg='white')
user_canvas = tk.Canvas(root, height=(cell_size * 11), width=(cell_size * 11), bg='white')

# Position the canvases
enemy_canvas.grid(row=0, column=0, padx=(10, 0), pady=10)
user_canvas.grid(row=0, column=1, padx=(10, 0), pady=10)

# Create grids on both canvases
create_grid(enemy_canvas, cell_size)
create_grid(user_canvas, cell_size)

# Add labels for the boards
tk.Label(root, text="ENEMY'S BOARD", fg="white", font=("Helvetica", 16)).grid(row=1, column=0)
tk.Label(root, text="USER SHIPS", fg="white", font=("Helvetica", 16)).grid(row=1, column=1)

# Ask user to enter direction
dir_prompt_label = tk.Label(root, text="Enter the direction you would like to place the ship in:",
                            font=("Helvetica", 14))
dir_prompt_label.grid(row=3, column=0, columnspan=2, pady=5)  # Adjust row, column, and other parameters as needed

# Display for the upcoming ship
shipLabel_text = tk.StringVar()
shipLabel_text.set(f"First ship to place: Aircraft Carrier (length: 5)")
shipLabel = tk.Label(root, textvariable=shipLabel_text, font=("Helvetica", 14))
shipLabel.grid(row=2, column=0, columnspan=2, pady=5)  # Adjust row, column, and other parameters as needed

# Display for direction of ship
dirLabel_text = tk.StringVar()
dirLabel_text.set(f"Current direction: U")
dirLabel = tk.Label(root, textvariable=dirLabel_text, font=("Helvetica", 14))
dirLabel.grid(row=4, column=0, columnspan=2, pady=5)  # Adjust row, column, and other parameters as needed

temp_label = tk.Label(root, font=("Helvetica", 20))
temp_label.grid(row=0, column=0, columnspan=2, pady=5)


# Function to set the selected direction
def set_direction(direction):
    global selected_direction
    selected_direction = direction
    dirLabel_text.set(f"Current direction: {direction}")


# Create buttons for directions
button_up = tk.Button(root, text="UP", command=lambda: set_direction("U"))
button_up.grid(row=6, column=0, columnspan=2, pady=5)

button_down = tk.Button(root, text="DOWN", command=lambda: set_direction("D"))
button_down.grid(row=7, column=0, columnspan=2, pady=5)

button_left = tk.Button(root, text="LEFT", command=lambda: set_direction("L"))
button_left.grid(row=8, column=0, columnspan=2, pady=5)

button_right = tk.Button(root, text="RIGHT", command=lambda: set_direction("R"))
button_right.grid(row=9, column=0, columnspan=2, pady=5)

# Bind the click event to the user canvas
user_canvas.bind('<Button-1>', on_user_canvas_click)

# Initialize the game board using Dynamic Programming
game_board = [[0 for _ in range(10)] for _ in range(10)]

# Initialize the ship queue
ship_queue = deque([
    Ship("Aircraft Carrier", 5),
    Ship("Battleship", 4),
    Ship("Cruiser", 3),
    Ship("Submarine", 3),
    Ship("Destroyer", 2)
])
current_ship = ship_queue[0] if ship_queue else None
# Initialize the game board for the enemy (CPU)
enemy_game_board = [[0] * 10 for _ in range(10)]

# Place CPU ships on the board
place_cpu_ships_on_board(enemy_game_board)

root.mainloop()
