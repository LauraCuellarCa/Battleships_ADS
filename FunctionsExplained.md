# Battleships Functions
## Below you can find the functions used across the 'main.py', 'cpu.py', 'Rankings.py', and 'welcomeWindow.py' files, along with their explanations and time complexities.

### User Ship Placement:

1. **`create_grid(canvas, cell_size):`**
   - Creates a grid on the given canvas with specified cell size.
   - It iteratively draws lines using a for-loop, so therefore the time complexity of this function is O(n), where n is the number of cells in one dimension of the grid.

2. **`is_valid_placement(ship_length, start_row, start_col, direction, board):`**
   - Checks if a ship can be placed at the specified location on the board.

3. **`show_temporary_label(text, duration):`**
   - Displays a temporary label for 3 seconds warning the user that their chosen ship placement is invalid and to please try again. 

4. **`clear_temporary_label():`**
   - Clears the temporary warning label.

5. **`draw_ship_on_canvas(canvas, ship_length, start_row, start_col, direction):`**
   - Draws a ship on the canvas based on its length, starting position, and direction.
   - It uses simple iterative constructs, similar to the create_grid function.
   - The time complexity of this function is O(n), where n is the length of the ship, as it iteratively draws each segment of the ship proportional to its length.

6. **`on_user_canvas_click(event):`**
   - Handles the user's click on the user canvas during ship placement.

### CPU Opponent:
1. **`__init__(self, board_size=10):`**
   - Initializes an instance of the `CPU_Player` class with a specified or default board size.
  
2. **`update_board(self, row, col, result):`**
   - Updates the CPU player's board based on the result of a shot (Hit or Miss).
  
3. **`determine_hit_directions(self, row, col):`**
   - Determines the possible hit directions for the CPU player to continue targeting a ship.
  
4. **`switch_hit_direction(self):`**
   - Switches the hit direction if the current direction reaches a dead-end.
  
5. **`choose_shot(self):`**
   - Chooses the next shot based on the current targeting mode or takes a random shot if not in target mode.
  
6. **`random_shot(self):`**
   - Generates a random shot (row, col) on the CPU player's board.
  
7. **`reset_target_mode(self):`**
   - Resets the target mode, clearing hit information and preparing for a new round.

### Battle Phase:
1. **`cpu_turn():`**
    - Depending on the current_turn, this function activates all the functions of the cpu.
    - The time complexity is O(1), depending on the functions it activates.

2. **`get_random_shot():`**
    - Gets a random shot for the CPU.
    - This function uses random number generation and the time complexity is O(1) as it computes the random shot in constant time.

3. **`process_cpu_shot(row, col):`**
    - Processes the CPU's shot by updating the game board based on whether a hit or miss occurred.
    - Its time complexity is O(1), as it involves direct access and update of array elements.

4. **`process_shot(row, col):`**
    - This function processes the user's shot and updates the enemy game board.
    - It also operates with a time complexity of O(1), involving direct array element manipulation without complex algorithms.

5. **`display_hit_or_miss(canvas, col, row, result):`**
    - Displays the result of a shot (hit or miss) on the canvas.
    - As it is mostly a UI affecting function, its time complexity depends on the underlying graphics but can be considered O(1) for the logic part of updating a single grid cell.

### Game Management:
1. **`create_ranking_system():`**
    - Creates a ranking system for tracking player performance.

2. **`display_rankings(ranking_system):`**
    - Displays player rankings in a new Tkinter window.

3. **`restart_game():`**
    - Restarts the game by saving data and running the `main.py` script again.
    - This function is called after the user presses the "Play again" button from the rankings window. 

### CPU Ship Placement:
1. **`place_cpu_ships_on_board(enemy_game_board):`**
   - Places CPU ships on the game board.

2. **`place_ships(grid, ships_to_place, placement_stack):`**
    - Recursively places ships on the grid, ensuring valid placement.

3. **`can_place_ship(grid, x, y, ship_size, orientation):`**
    - Checks if a ship can be placed at the specified location.

4. **`place_ship(grid, x, y, ship_size, orientation):`**
    - Places a ship on the grid at the specified location.

5. **`remove_ship(grid, x, y, ship_size, orientation):`**
    - Removes a ship from the grid.

6. **`all_ships_placed(grid):`**
    - Checks if all ships have been placed on the grid.

### Ranking System:
1. **`__init__(self):`**
   - Initializes an instance of the `RankingSystem` class with an empty dictionary for players.

2. **`add_player(self, player_name):`**
   - Adds a new player to the ranking system with initial play and win counts.

3. **`record_play(self, player_name, won=False):`**
   - Records a play for the specified player, increments play count, and, if applicable, win count.
   - Checks if the player already exists in the dictionary, and if so, it updates their play/win count. Otherwise, it calls on the 'add_player' function and adds them to the player dictionary with initial values. 
     
4. **`merge_sort(self, player_list):`**
   - Performs the merge sort algorithm on the list of players, sorting them based on the number of wins.
   - recursively divides the player_list into smaller halves until each subarray has only one element (which is inherently sorted). Then, it merges these sorted subarrays back together in a way that ensures the final merged array is sorted. More detailed explanation here --> 

5. **`get_ranking(self):`**
   - Returns a sorted list of players based on their win counts.
   - Calls on the merge_sort algorithm and passes in the current player_list as a parameter. 

6. **`save_data(self):`**
   - Saves the ranking system data (players and their stats) to a JSON file named "player_data.json."

7. **`load_data(self):`**
   - Loads the ranking system data from the "player_data.json" file.
   - return empty data if the file is not found. 

8. **`load_existing_players(self):`**
   - Loads existing player data at the beginning of the game. Calls `load_data()` internally.
   - Implemented to keep game history up to date everytime the user choses to "play again"
   

### Welcome Window

1. **`create_welcome_window():`**
   - Creates a welcome window for the Battleships Game using Tkinter.
  
2. **`get_player_name_start_game(playerName, root):`**
   - Gets the player name entered in the welcome window and starts the game. Closes the welcome window.



