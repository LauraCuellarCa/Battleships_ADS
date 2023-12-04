# Battleships Functions
## Below you can find the functions used across the 'main.py', 'cpu.py', 'Rankings.py', and 'welcomeWindow.py' files, along with their explanations and time complexities.

### User Ship Placement:

1. **`create_grid(canvas, cell_size):`**
   - Creates a grid on the given canvas with specified cell size.
   - It iteratively draws lines using a for-loop, so therefore the time complexity of this function is O(n), where n is the number of cells in one dimension of the grid.

2. **`is_valid_placement(ship_length, start_row, start_col, direction, board):`**
   - Checks if a ship can be placed at the specified location on the board.
   - The function has a loop that iterates over the range of ship_length for each direction (Right, Left, Down, Up). In each iteration of the loop, the function performs constant-time operations (comparisons and indexing) to check if the placement is valid.
   - Time complexity of O(n), where n is the ship_length of the ship being placed on the board.

3. **`show_temporary_label(text, duration):`**
   - Displays a temporary label for 3 seconds warning the user that their chosen ship placement is invalid and to please try again.
   - The temp_label.config operation sets the text, foreground color (fg), and background color (bg) of the temp_label widget. This operation is constant time since it involves updating the attributes of a GUI element. The temp_label.after(duration, clear_temporary_label) schedules the clear_temporary_label function to be called after a certain duration. This is also a constant-time operation. Therefore, the time complexity of show_temporary_label is constant, O(1).

4. **`clear_temporary_label():`**
   - Clears the temporary warning label.
   - The temp_label.config operation sets the text to an empty string and changes the background color. Like in the show_temporary_label function, this operation is constant time. The time complexity of clear_temporary_label is also constant, O(1).

5. **`draw_ship_on_canvas(canvas, ship_length, start_row, start_col, direction):`**
   - Draws a ship on the canvas based on its length, starting position, and direction.
   - It uses simple iterative constructs, similar to the create_grid function.
   - The time complexity of this function is O(n), where n is the length of the ship, as it iteratively draws each segment of the ship proportional to its length.

6. **`on_user_canvas_click(event):`**
   - Handles the user's click on the user canvas during ship placement. Checks if it is a valid placement, updates the board, and perform dequeue() operations.
   - Because the dominant factor of this functions is the validation and updating steps (both proportional to the length of the ship), the overall time complexity of the on_user_canvas_click function is O(n) where n is ship_length.

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

### CPU Ship Placement:
1. **`place_cpu_ships_on_board(enemy_game_board):`**
   - Places CPU ships on the game board using specified ship sizes. Utilizes the place_ships function.
   - Time Complexity: Depends on the efficiency of place_ships

2. **`place_ships(grid, ships_to_place, placement_stack):`**
    - Recursively attempts to place ships on the game board using a backtracking algorithm if needed. It explores different orientations and positions for the starting point until a valid placement is found or all possibilities are tried out.
    - The function uses a while loop to attempt placements until all ships are placed or it determines that a valid placement is not possible.   Inside the loop, it randomises the ship orientation and position and checks if the ship can be placed without violating the rules. If successful, the ship is added to the board, and the recursive call continues for the remaining ships. If not, the algorithm backtracks by removing the last attempted placement and trying a different one. 
    - Time Complexity: The time complexity depends on the efficiency of the backtracking algorithm and randomisation due to the recursive nature of the algorithm, worst case O notation is exponential, best case O(1).

3. **`can_place_ship(grid, x, y, ship_size, orientation):`**
    - Helper funtion for place_ships that checks if a ship can be placed at the specified position without violating rules.
    - Time Complexity: O(n) with n being ship_size.

4. **`place_ship(grid, x, y, ship_size, orientation):`**
    - Helper function for place_ships that places a ship on the grid at the specified location changing the value of the corresponding cells on the game board to indicate the presence of the ship.
    - Time Complexity: O(n) with n being ship_size.

5. **`remove_ship(grid, x, y, ship_size, orientation):`**
    - Helper function for the place_ships function. It is used for backtracking and removes a previously placed ship from the game board.
    - Time Complexity: O(n) with n being ship_size.

6. **`all_ships_placed(grid):`**
    - Checks if all ships have been placed on the grid by comparing the summation of cell values to summation of ship lengths.
    - Time Complexity: O(1).

### Ranking System:
1. **`__init__(self):`**
   - Initializes an instance of the `RankingSystem` class with an empty dictionary for players.

2. **`add_player(self, player_name):`**
   - Adds a new player to the ranking system with initial play and win counts.
   - The time complexity of adding a player is O(1) because updating a dictionary with a constant number of operations.

3. **`record_play(self, player_name, won=False):`**
   - Records a play for the specified player, increments play count, and, if applicable, win count.
   - Checks if the player already exists in the dictionary, and if so, it updates their play/win count. Otherwise, it calls on the 'add_player' function and adds them to the player dictionary with initial values.
   - The time complexity of updating plays and wins for a player is O(1) because it involves updating values in a dictionary.
     
4. **`merge_sort(self, player_list):`**
   - Performs the merge sort algorithm on the list of players, sorting them based on the number of wins.
   - recursively divides the player_list into smaller halves until each subarray has only one element (which is inherently sorted). Then, it merges these sorted subarrays back together in a way that ensures the final merged array is sorted. More detailed explanation here.
   - The time complexity of merge sort is O(n log n), where n is the length of the player_list. This is due to the recursive nature of the algorithm.

5. **`get_ranking(self):`**
   - Returns a sorted list of players based on their win counts.
   - Calls on the merge_sort algorithm and passes in the current player_list as a parameter.
   - Calls merge_sort, so the time complexity is O(n log n), where n is the number of players.

6. **`save_data(self):`**
   - Saves the ranking system data (players and their stats) to a JSON file named "player_data.json."
   - The time complexity of saving data to a file is O(n), where n is the number of players. This is because it involves iterating over the players and writing their data to a file.

7. **`load_data(self):`**
   - Loads the ranking system data from the "player_data.json" file.
   - return empty data if the file is not found.
   - The time complexity of loading data from a file is O(n), where n is the number of players. This is because it involves reading data from a file and updating the players' dictionary.

8. **`load_existing_players(self):`**
   - Loads existing player data at the beginning of the game. Calls `load_data()` internally.
   - Implemented to keep game history up to date everytime the user choses to "play again"
   - Calls load_data, so the time complexity is also O(n), where n is the number of players.
   - 
### Game Management:

1. **`display_rankings(ranking_system):`**
    - Displays player rankings in a new Tkinter window.
    - The time complexity of getting the ranking using the get_ranking method is O(n log n), where n is the number of players. This is because the get_ranking method uses the merge sort algorithm.
    - The loop that creates labels to display player information iterates over the ranking list, which has a length of n. The time complexity of this part is O(n).
    - the dominant factor in the time complexity is the sorting of the ranking, which is O(n log n). Therefore, the overall time complexity of the function is O(n log n).

2. **`restart_game():`**
    - Restarts the game by saving data and running the `main.py` script again.
    - This function is called after the user presses the "Play again" button from the rankings window.
    - The time complexity of saving data to a file depends on the number of players in the ranking system, n.
    - The subprocess.run function runs a new process to restart the game by executing the 'main.py' script. The time complexity of this operation can be denoted as denoted as O(m) for simplicity, where m is the complexity of the 'main.py' script.
    - The overall time complexity of the restart_game function can be expressed as O(n + m), where n is the number of players in the ranking system, and m is the complexity of the 'main.py' script.

   

### Welcome Window

1. **`create_welcome_window():`**
   - Creates a welcome window for the Battleships Game using Tkinter.
   - Creating a Tkinter window, labels, entry widget, and a button involves constant-time operations. Therefore, the overall time complexity of create_welcome_window is O(1).
  
2. **`get_player_name_start_game(playerName, root):`**
   - Gets the player name entered in the welcome window and starts the game. Closes the welcome window.
   - Assigning the global variable player_name is a constant-time operation. Destroying the Tkinter window (root.destroy()) is also a constant-time operation. Therefore, the overall time complexity of get_player_name_start_game is O(1).



